from django.db.utils import OperationalError

__author__ = 'yeray'
from django.core.management.base import BaseCommand
from core.models import PagelinkPost
from phasionate.models import WpPosts
from twitter_bots_prod.models import ProjectPagelink, ProjectProject
from igoo_co.models import RedirectPage
import logging

logger_sync = logging.getLogger(__name__)

wp_posts = {}


def insert_pagelink_id_in_default_db(post_data, new_pagelink):
    logger_sync.info(
        'Inserting pagelink id por post "%s" in table pagelink_post in default db ...' % post_data['title'])

    pagelink_for_post = ProjectPagelink.objects.using('twitter_bots_prod').get(page_title=post_data['title'],
                                                                               page_link=new_pagelink.page_link)
    pagelink_post_to_change = PagelinkPost.objects.using('default').get(post_id=post_data['post_id'])
    pagelink_post_to_change.pagelink_id = pagelink_for_post.id
    pagelink_post_to_change.save()

    new_pagelink_post = PagelinkPost.objects.using('default').filter(pagelink_id=pagelink_for_post.id,
                                                                  post_id=post_data['post_id'])
    if new_pagelink_post.exists():
        logger_sync.info(
            'OK: Pagelink id por post "%s" in table pagelink_post in default db inserted succesfully' % post_data[
                'title'])
    else:
        logger_sync.error(
            'Insert Pagelink id por post "%s" in table pagelink_post in default db failed ...' % post_data['title'])


def create_short_link(post_data):
    from django.utils.crypto import get_random_string

    logger_sync.info('Creating shortlink por post "%s"  in igoo_co db ...' % post_data['title'])

    uri = get_random_string(length=5)

    while RedirectPage.objects.using('igoo_co').filter(uri=uri).exists():
        uri = get_random_string(length=5)

    new_redirect_page, created = RedirectPage.objects.using('igoo_co').get_or_create(
        all=post_data['link'],
        defaults={
            'card_img_url': post_data['image'],
            'uri': uri,
            'card_title': post_data['title'],
            # 'card_description': post_data['description'],
        },
    )

    if created:
        logger_sync.info('Success on Creating shortlink por post "%s"  in igoo_co db' % post_data['title'])

        return 'http://igoo.co/%s' % uri
    else:
        logger_sync.info(
            'Shortlink por post "%s"  in igoo_co db already exist. Using this short link' % post_data['title'])

        return 'http://igoo.co/%s' % new_redirect_page.uri


def get_project_instance(post_data):
    logger_sync.info(
        'Getting project instance "phasionate" for post "%s"  in twitter_bots_prod db ...' % post_data['title'])
    try:
        project = ProjectProject.objects.using('twitter_bots_prod').filter(id=6)
    except OperationalError as e:
        logger_sync.error('%s' % e.message)
        logger_sync.info('Trying to reconnect ...')
        project = ProjectProject.objects.using('twitter_bots_prod').get(id=6)

    if project.exists():
        logger_sync.info('Project obtained')
        return project[0]
    else:
        logger_sync.error('Error while obtaining Project')


def create_pagelink(post_data):
    logger_sync.info('Creating pagelink for post "%s" in twitter_bots_prod db ...' % post_data['title'])

    new_pagelink, created = ProjectPagelink.objects.using('twitter_bots_prod').get_or_create(
        page_title=post_data['title'],
        project=get_project_instance(post_data),
        is_active=1,
        language='es',
        defaults={'page_link': create_short_link(post_data)},
    )

    if created:
        logger_sync.info('Success on creating pagelink for post "%s" in twitter_bots_prod db' % post_data['title'])
    else:
        logger_sync.info(
            'Pagelink for post "%s" in twitter_bots_prod db already exist. Using this pagelink' % post_data['title'])

    return new_pagelink

    # try:
    # return ProjectPagelink(
    # page_title=post_data.title,
    # page_link=create_short_link(post_data),
    # project=get_project_instance(post_data),
    # is_active=1,
    # language='es',
    # )
    # except Exception, e:
    # logger_sync.error('Error creating pagelink for post "%s"' % post_data.title)
    # raise e


def get_post_image(wp_post):
    logger_sync.info('Looking for post "%s" image in phasionate db ...' % wp_post.post_title)
    wp_post_image = wp_posts.filter(post_parent=wp_post.id, post_type='attachment', post_mime_type='image/jpeg')

    if wp_post_image.exists():
        logger_sync.info('Image found for post "%s" in phasionate db' % wp_post.post_title)
        return wp_post_image[0].guid
    else:
        logger_sync.warning('No image found for post "%s" in phasionate db' % wp_post.post_title)
        return None


def fetch_post_data(wp_post):
    logger_sync.info('Fetching data for post "%s" ...' % wp_post.post_title)

    try:
        return {
            'post_id': wp_post.id,
            'link': wp_post.guid,
            'title': wp_post.post_title,
            'description': wp_post.post_excerpt,
            'image': get_post_image(wp_post),
            'hashtag': None,
        }
    except Exception, e:
        logger_sync.error('Error creating obj for post "%s"' % wp_post.post_title)
        raise e


def sync_post(wp_post):
    logger_sync.info('---- Sync process for "%s" started ----' % wp_post.post_title)
    # 2 Recolectar los datos de los post que aun no tienen pagelink
    # 3 Crear link corto mediante igoo.co
    post_data = fetch_post_data(wp_post)
    # 4 crear pagelink
    new_pagelink = create_pagelink(post_data)
    # new_pagelink.save()
    # 5 Incluir el id del pagelink en la tabla pagelink post
    insert_pagelink_id_in_default_db(post_data, new_pagelink)
    logger_sync.info('---- Sync process for "%s" finished ----\n\n' % wp_post.post_title)


def check_pagelinkposts_for_post(post_in_default_db, wp_post):
    logger_sync.info('Checking pagelink_post for post "%s"  in default db ...' % wp_post.post_title)

    if post_in_default_db.pagelink_id:
        try:
            ProjectPagelink.objects.using('twitter_bots_prod').get(id=post_in_default_db.pagelink_id)
            logger_sync.info('Pagelink_post exist for post "%s" in default db\n\n' % wp_post.post_title)

            return True

        except ProjectPagelink.DoesNotExist:
            logger_sync.info('Pagelink_post does not exist for post "%s" in default db' % wp_post.post_title)

            return False
    else:
        logger_sync.info('Pagelink_post does not exist for post "%s" in default db' % wp_post.post_title)
        return False


def put_post_id_in_default_db(wp_post):
    logger_sync.info('Checking if post "%s" is in pagelink_post table in default db ...' % wp_post.post_title)
    post_in_db, created = PagelinkPost.objects.using('default').get_or_create(post_id=wp_post.id)

    if created:
        logger_sync.info('NEW POST: post "%s" succesfully inserted in default db' % wp_post.post_title)
    else:
        logger_sync.info('Post "%s" already exist in default db' % wp_post.post_title)

    return post_in_db, created


def get_published_posts():
    logger_sync.info('Getting published posts from Phasionate db ... ')
    global wp_posts
    try:
        wp_posts = WpPosts.objects.using('phasionate').all()
    except OperationalError as e:
        logger_sync.error('%s' % e.message)
        logger_sync.info('Trying to reconnect ...')
        wp_posts = WpPosts.objects.using('phasionate').all()

    if wp_posts.exists():
        logger_sync.info('Posts obtained\n\n')
        return wp_posts.filter(post_status='publish', post_type='post')


def sync_pagelinks():
    # 1 Obtener todos los ids de los post de phasionate, introducirlos en la tabla pagelink_ost (default db)
    # y comprobar si tienen pagelink

    for wp_post in get_published_posts():
        logger_sync.info('**************  %s  **************' % wp_post.post_title)
        post_in_default_db, created = put_post_id_in_default_db(wp_post)

        if not created:
            if not check_pagelinkposts_for_post(post_in_default_db, wp_post):
                sync_post(wp_post)
        else:
            sync_post(wp_post)


class Command(BaseCommand):
    help = 'Create pagelink for new phasionate posts'

    def handle(self, *args, **options):
        logger_sync.info('Sync Pagelinks launched')
        sync_pagelinks()