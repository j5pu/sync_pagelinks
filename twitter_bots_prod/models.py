# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import twitter_bots_prod


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class CoreProxy(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    proxy = models.CharField(max_length=21)
    proxy_provider = models.CharField(max_length=50)
    is_unavailable_for_registration = models.IntegerField()
    date_unavailable_for_registration = models.DateTimeField(blank=True, null=True)
    is_unavailable_for_use = models.IntegerField()
    date_unavailable_for_use = models.DateTimeField(blank=True, null=True)
    is_phone_required = models.IntegerField()
    date_phone_required = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()
    is_in_proxies_txts = models.IntegerField()
    date_not_in_proxies_txts = models.DateTimeField(blank=True, null=True)
    proxies_group = models.ForeignKey('ProjectProxiesgroup', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_proxy'


class CoreTwitterbot(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    real_name = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    username = models.CharField(max_length=50)
    date = models.DateTimeField()
    password_twitter = models.CharField(max_length=20)
    is_manually_registered = models.IntegerField()
    password_email = models.CharField(max_length=20)
    user_agent = models.TextField()
    birth_date = models.DateField(blank=True, null=True)
    gender = models.IntegerField()
    date_suspended_email = models.DateTimeField(blank=True, null=True)
    date_suspended_twitter = models.DateTimeField(blank=True, null=True)
    email_registered_ok = models.IntegerField()
    twitter_registered_ok = models.IntegerField()
    twitter_confirmed_email_ok = models.IntegerField()
    twitter_avatar_completed = models.IntegerField()
    twitter_bio_completed = models.IntegerField()
    is_suspended = models.IntegerField()
    is_suspended_email = models.IntegerField()
    is_being_created = models.IntegerField()
    is_dead = models.IntegerField()
    proxy_for_registration = models.ForeignKey(CoreProxy, related_name='twitter_bot', blank=True, null=True)
    date_death = models.DateTimeField(blank=True, null=True)
    # proxy_for_usage = models.ForeignKey(CoreProxy, related_name='twitter_bot', blank=True, null=True)
    num_suspensions_lifted = models.IntegerField()
    is_following = models.IntegerField()
    date_last_following = models.DateTimeField(blank=True, null=True)
    following_ratio = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_twitterbot'


class CoreUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_user'


class CoreUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(CoreUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'core_user_groups'


class CoreUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(CoreUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'core_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ProjectExtractor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    consumer_key = models.CharField(max_length=200)
    consumer_secret = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    twitter_bot = models.ForeignKey(CoreTwitterbot, unique=True)
    last_request_date = models.DateTimeField(blank=True, null=True)
    is_rate_limited = models.IntegerField()
    minutes_window = models.IntegerField(blank=True, null=True)
    mode = models.IntegerField()
    is_suspended = models.IntegerField()
    date_suspended = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_extractor'


class ProjectFeed(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'project_feed'


class ProjectFeeditem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    feed = models.ForeignKey(ProjectFeed)
    text = models.CharField(max_length=101)
    link = models.CharField(max_length=200, blank=True)
    date_saved = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_feeditem'


class ProjectFeedsgroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'project_feedsgroup'


class ProjectFeedsgroupFeeds(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    feedsgroup = models.ForeignKey(ProjectFeedsgroup)
    feed = models.ForeignKey(ProjectFeed)

    class Meta:
        managed = False
        db_table = 'project_feedsgroup_feeds'


class ProjectFeedsgroupProxiesGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    feedsgroup = models.ForeignKey(ProjectFeedsgroup)
    proxiesgroup = models.ForeignKey('ProjectProxiesgroup')

    class Meta:
        managed = False
        db_table = 'project_feedsgroup_proxies_groups'


class ProjectFollower(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    target_user = models.ForeignKey('ProjectTargetuser')
    twitter_user = models.ForeignKey('ProjectTwitteruser')
    date_saved = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_follower'


class ProjectFtweetsnumpertumention(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number = models.IntegerField()
    tu_mention = models.ForeignKey('ProjectTweet', unique=True)

    class Meta:
        managed = False
        db_table = 'project_ftweetsnumpertumention'


class ProjectHashtag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    q = models.CharField(max_length=140)
    geocode = models.CharField(max_length=50, blank=True)
    lang = models.CharField(max_length=2, blank=True)
    result_type = models.IntegerField()
    max_id = models.BigIntegerField(blank=True, null=True)
    older_limit_for_tweets = models.DateTimeField(blank=True, null=True)
    max_user_count = models.IntegerField(blank=True, null=True)
    is_extracted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_hashtag'


class ProjectHashtaggroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=140)

    class Meta:
        managed = False
        db_table = 'project_hashtaggroup'


class ProjectHashtaggroupHashtags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    hashtaggroup = models.ForeignKey(ProjectHashtaggroup)
    hashtag = models.ForeignKey(ProjectHashtag)

    class Meta:
        managed = False
        db_table = 'project_hashtaggroup_hashtags'


class ProjectHashtaggroupProjects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    hashtaggroup = models.ForeignKey(ProjectHashtaggroup)
    project = models.ForeignKey('ProjectProject')

    class Meta:
        managed = False
        db_table = 'project_hashtaggroup_projects'


class ProjectLink(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=200)
    project = models.ForeignKey('ProjectProject', blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_link'


class ProjectPagelink(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    page_title = models.CharField(max_length=150, blank=True)
    page_link = models.CharField(max_length=200)
    project = models.ForeignKey('twitter_bots_prod.ProjectProject')
    is_active = models.IntegerField()
    image = models.ForeignKey('twitter_bots_prod.ProjectTweetimg')
    language = models.CharField(max_length=2, blank=True)

    def __unicode__(self):
        return self.page_title

    class Meta:
        managed = False
        db_table = 'project_pagelink'


class ProjectPagelinkHashtags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pagelink = models.ForeignKey(ProjectPagelink)
    pagelinkhashtag = models.ForeignKey('ProjectPagelinkhashtag')

    class Meta:
        managed = False
        db_table = 'project_pagelink_hashtags'


class ProjectPagelinkhashtag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'project_pagelinkhashtag'


class ProjectProject(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    has_tracked_clicks = models.IntegerField(null=True, db_index=True)
    is_running = models.IntegerField(null=True, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'project_project'


class ProjectProjectHashtags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    project = models.ForeignKey('ProjectProject')
    hashtag = models.ForeignKey(ProjectHashtag)

    class Meta:
        managed = False
        db_table = 'project_project_hashtags'


class ProjectProjectTargetUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    project = models.ForeignKey(ProjectProject)
    targetuser = models.ForeignKey('ProjectTargetuser')

    class Meta:
        managed = False
        db_table = 'project_project_target_users'


class ProjectProxiesgroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    max_tw_bots_per_proxy_for_registration = models.IntegerField()
    max_tw_bots_per_proxy_for_usage = models.IntegerField()
    time_between_tweets = models.CharField(max_length=10)
    max_num_mentions_per_tweet = models.IntegerField()
    min_days_between_registrations_per_proxy = models.IntegerField()
    webdriver = models.CharField(max_length=2)
    is_bot_creation_enabled = models.IntegerField()
    is_bot_usage_enabled = models.IntegerField()
    has_tweet_msg = models.IntegerField()
    has_link = models.IntegerField()
    has_tweet_img = models.IntegerField()
    has_page_announced = models.IntegerField()
    has_mentions = models.IntegerField()
    reuse_proxies_with_suspended_bots = models.IntegerField()
    min_days_between_registrations_per_proxy_under_same_subnet = models.IntegerField()
    num_consecutive_mentions_for_check_mentioning_works = models.IntegerField()
    mention_fail_time_window = models.CharField(max_length=10)
    destination_bot_checking_time_window = models.CharField(max_length=10)
    feedtweets_per_twitteruser_mention = models.CharField(max_length=10)
    mctweet_to_same_bot_time_window = models.CharField(max_length=10)
    following_ratio = models.CharField(max_length=10)
    time_window_to_follow = models.CharField(max_length=10)
    max_num_users_to_follow_at_once = models.CharField(max_length=10)
    has_following_activated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_proxiesgroup'


class ProjectProxiesgroupProjects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    proxiesgroup = models.ForeignKey(ProjectProxiesgroup)
    project = models.ForeignKey(ProjectProject)

    class Meta:
        managed = False
        db_table = 'project_proxiesgroup_projects'


class ProjectSublink(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=200)
    parent_link = models.ForeignKey(ProjectLink)
    platform = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'project_sublink'


class ProjectTargetuser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(max_length=80)
    next_cursor = models.BigIntegerField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    extractor_used = models.ForeignKey(ProjectExtractor, blank=True, null=True)
    is_active = models.IntegerField()
    date_extraction_end = models.DateTimeField(blank=True, null=True)
    num_consecutive_pages_without_enough_new_followers = models.IntegerField(blank=True, null=True)
    date_last_extraction = models.DateTimeField(blank=True, null=True)
    is_suspended = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_targetuser'


class ProjectTugroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=140)

    class Meta:
        managed = False
        db_table = 'project_tugroup'


class ProjectTugroupProjects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tugroup = models.ForeignKey(ProjectTugroup)
    project = models.ForeignKey(ProjectProject)

    class Meta:
        managed = False
        db_table = 'project_tugroup_projects'


class ProjectTugroupTargetUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tugroup = models.ForeignKey(ProjectTugroup)
    targetuser = models.ForeignKey(ProjectTargetuser)

    class Meta:
        managed = False
        db_table = 'project_tugroup_target_users'


class ProjectTweet(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    project = models.ForeignKey(ProjectProject, blank=True, null=True)
    tweet_msg = models.ForeignKey('ProjectTweetmsg', blank=True, null=True)
    link = models.ForeignKey(ProjectLink, blank=True, null=True)
    sent_ok = models.IntegerField()
    sending = models.IntegerField()
    date_created = models.DateTimeField()
    date_sent = models.DateTimeField(blank=True, null=True)
    bot_used = models.ForeignKey(CoreTwitterbot, blank=True, null=True)
    page_announced = models.ForeignKey(ProjectPagelink, blank=True, null=True)
    tweet_img = models.ForeignKey('ProjectTweetimg', blank=True, null=True)
    feed_item = models.ForeignKey(ProjectFeeditem, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tweet'


class ProjectTweetMentionedBots(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tweet = models.ForeignKey(ProjectTweet)
    twitterbot = models.ForeignKey(CoreTwitterbot)

    class Meta:
        managed = False
        db_table = 'project_tweet_mentioned_bots'


class ProjectTweetMentionedUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tweet = models.ForeignKey(ProjectTweet)
    twitteruser = models.ForeignKey('ProjectTwitteruser')

    class Meta:
        managed = False
        db_table = 'project_tweet_mentioned_users'


class ProjectTweetcheckingmention(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tweet = models.ForeignKey(ProjectTweet, unique=True)
    mentioning_works = models.IntegerField()
    destination_bot_is_checking_mention = models.IntegerField()
    destination_bot_checked_mention = models.IntegerField()
    destination_bot_checked_mention_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tweetcheckingmention'


class ProjectTweetfromfeed(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tweet = models.ForeignKey(ProjectTweet, related_name='tweed_from_feed', unique=True)
    # tu_mention = models.ForeignKey(ProjectTweet, related_name='tweed_from_feed')

    class Meta:
        managed = False
        db_table = 'project_tweetfromfeed'


class ProjectTweetimg(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    img = models.CharField(max_length=100, blank=True)
    is_using = models.IntegerField()
    project = models.ForeignKey(ProjectProject)

    def __unicode__(self):
        return self.img

    class Meta:
        managed = False
        db_table = 'project_tweetimg'


class ProjectTweetmsg(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.CharField(max_length=101)
    project = models.ForeignKey(ProjectProject, blank=True, null=True)
    language = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'project_tweetmsg'


class ProjectTwitterbotfollowing(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    bot = models.ForeignKey(CoreTwitterbot)
    twitteruser = models.ForeignKey('ProjectTwitteruser')
    performed_follow = models.IntegerField()
    followed_ok = models.IntegerField()
    date_followed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_twitterbotfollowing'


class ProjectTwitteruser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    source = models.IntegerField()
    username = models.CharField(max_length=160)
    twitter_id = models.BigIntegerField()
    country = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=2)
    city = models.CharField(max_length=80, blank=True)
    created_date = models.DateTimeField()
    full_name = models.CharField(max_length=160, blank=True)
    geo_enabled = models.IntegerField()
    time_zone = models.CharField(max_length=50, blank=True)
    last_tweet_date = models.DateTimeField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    tweets_count = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField()
    date_saved = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_twitteruser'


class ProjectTwitteruserNew(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    source = models.IntegerField()
    username = models.CharField(max_length=160)
    twitter_id = models.BigIntegerField()
    country = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=2)
    city = models.CharField(max_length=80, blank=True)
    created_date = models.DateTimeField()
    full_name = models.CharField(max_length=160, blank=True)
    geo_enabled = models.IntegerField()
    time_zone = models.CharField(max_length=50, blank=True)
    last_tweet_date = models.DateTimeField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    tweets_count = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField()
    date_saved = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_twitteruser_new'


class ProjectTwitteruserhashashtag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    hashtag = models.ForeignKey(ProjectHashtag)
    twitter_user = models.ForeignKey(ProjectTwitteruser)
    date_saved = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_twitteruserhashashtag'


class ProjectViewTwitterUser(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    source = models.IntegerField()
    username = models.CharField(max_length=160)
    twitter_id = models.BigIntegerField()
    country = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=2)
    city = models.CharField(max_length=80, blank=True)
    created_date = models.DateTimeField()
    full_name = models.CharField(max_length=160, blank=True)
    geo_enabled = models.IntegerField()
    time_zone = models.CharField(max_length=50, blank=True)
    last_tweet_date = models.DateTimeField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    tweets_count = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField()
    date_saved = models.DateTimeField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_view_twitter_user'


class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'
