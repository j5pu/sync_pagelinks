# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoreProxy',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('proxy', models.CharField(max_length=21)),
                ('proxy_provider', models.CharField(max_length=50)),
                ('is_unavailable_for_registration', models.IntegerField()),
                ('date_unavailable_for_registration', models.DateTimeField(null=True, blank=True)),
                ('is_unavailable_for_use', models.IntegerField()),
                ('date_unavailable_for_use', models.DateTimeField(null=True, blank=True)),
                ('is_phone_required', models.IntegerField()),
                ('date_phone_required', models.DateTimeField(null=True, blank=True)),
                ('date_added', models.DateTimeField()),
                ('is_in_proxies_txts', models.IntegerField()),
                ('date_not_in_proxies_txts', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'core_proxy',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoreTwitterbot',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('real_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('password_twitter', models.CharField(max_length=20)),
                ('is_manually_registered', models.IntegerField()),
                ('password_email', models.CharField(max_length=20)),
                ('user_agent', models.TextField()),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('gender', models.IntegerField()),
                ('date_suspended_email', models.DateTimeField(null=True, blank=True)),
                ('date_suspended_twitter', models.DateTimeField(null=True, blank=True)),
                ('email_registered_ok', models.IntegerField()),
                ('twitter_registered_ok', models.IntegerField()),
                ('twitter_confirmed_email_ok', models.IntegerField()),
                ('twitter_avatar_completed', models.IntegerField()),
                ('twitter_bio_completed', models.IntegerField()),
                ('is_suspended', models.IntegerField()),
                ('is_suspended_email', models.IntegerField()),
                ('is_being_created', models.IntegerField()),
                ('is_dead', models.IntegerField()),
                ('date_death', models.DateTimeField(null=True, blank=True)),
                ('num_suspensions_lifted', models.IntegerField()),
                ('is_following', models.IntegerField()),
                ('date_last_following', models.DateTimeField(null=True, blank=True)),
                ('following_ratio', models.DecimalField(null=True, max_digits=2, decimal_places=1, blank=True)),
            ],
            options={
                'db_table': 'core_twitterbot',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoreUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'core_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoreUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'core_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoreUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'core_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('user_id', models.IntegerField()),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectExtractor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('consumer_key', models.CharField(max_length=200)),
                ('consumer_secret', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=200)),
                ('access_token_secret', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
                ('last_request_date', models.DateTimeField(null=True, blank=True)),
                ('is_rate_limited', models.IntegerField()),
                ('minutes_window', models.IntegerField(null=True, blank=True)),
                ('mode', models.IntegerField()),
                ('is_suspended', models.IntegerField()),
                ('date_suspended', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'project_extractor',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFeed',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('url', models.CharField(unique=True, max_length=200)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'project_feed',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFeeditem',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=101)),
                ('link', models.CharField(max_length=200, blank=True)),
                ('date_saved', models.DateTimeField()),
            ],
            options={
                'db_table': 'project_feeditem',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFeedsgroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'project_feedsgroup',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFeedsgroupFeeds',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_feedsgroup_feeds',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFeedsgroupProxiesGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_feedsgroup_proxies_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFollower',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date_saved', models.DateTimeField()),
            ],
            options={
                'db_table': 'project_follower',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFtweetsnumpertumention',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'project_ftweetsnumpertumention',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectHashtag',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('q', models.CharField(max_length=140)),
                ('geocode', models.CharField(max_length=50, blank=True)),
                ('lang', models.CharField(max_length=2, blank=True)),
                ('result_type', models.IntegerField()),
                ('max_id', models.BigIntegerField(null=True, blank=True)),
                ('older_limit_for_tweets', models.DateTimeField(null=True, blank=True)),
                ('max_user_count', models.IntegerField(null=True, blank=True)),
                ('is_extracted', models.IntegerField()),
            ],
            options={
                'db_table': 'project_hashtag',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectHashtaggroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'project_hashtaggroup',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectHashtaggroupHashtags',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_hashtaggroup_hashtags',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectHashtaggroupProjects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_hashtaggroup_projects',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 'project_link',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectPagelink',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('page_title', models.CharField(max_length=150, blank=True)),
                ('page_link', models.CharField(max_length=200)),
                ('is_active', models.IntegerField()),
                ('language', models.CharField(max_length=2, blank=True)),
            ],
            options={
                'db_table': 'project_pagelink',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectPagelinkhashtag',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'project_pagelinkhashtag',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectPagelinkHashtags',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_pagelink_hashtags',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProject',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('has_tracked_clicks', models.IntegerField(null=True, db_index=True)),
                ('is_running', models.IntegerField(null=True, db_index=True)),
            ],
            options={
                'db_table': 'project_project',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProjectHashtags',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_project_hashtags',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProjectTargetUsers',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_project_target_users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProxiesgroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('max_tw_bots_per_proxy_for_registration', models.IntegerField()),
                ('max_tw_bots_per_proxy_for_usage', models.IntegerField()),
                ('time_between_tweets', models.CharField(max_length=10)),
                ('max_num_mentions_per_tweet', models.IntegerField()),
                ('min_days_between_registrations_per_proxy', models.IntegerField()),
                ('webdriver', models.CharField(max_length=2)),
                ('is_bot_creation_enabled', models.IntegerField()),
                ('is_bot_usage_enabled', models.IntegerField()),
                ('has_tweet_msg', models.IntegerField()),
                ('has_link', models.IntegerField()),
                ('has_tweet_img', models.IntegerField()),
                ('has_page_announced', models.IntegerField()),
                ('has_mentions', models.IntegerField()),
                ('reuse_proxies_with_suspended_bots', models.IntegerField()),
                ('min_days_between_registrations_per_proxy_under_same_subnet', models.IntegerField()),
                ('num_consecutive_mentions_for_check_mentioning_works', models.IntegerField()),
                ('mention_fail_time_window', models.CharField(max_length=10)),
                ('destination_bot_checking_time_window', models.CharField(max_length=10)),
                ('feedtweets_per_twitteruser_mention', models.CharField(max_length=10)),
                ('mctweet_to_same_bot_time_window', models.CharField(max_length=10)),
                ('following_ratio', models.CharField(max_length=10)),
                ('time_window_to_follow', models.CharField(max_length=10)),
                ('max_num_users_to_follow_at_once', models.CharField(max_length=10)),
                ('has_following_activated', models.IntegerField()),
            ],
            options={
                'db_table': 'project_proxiesgroup',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProxiesgroupProjects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_proxiesgroup_projects',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectSublink',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('platform', models.IntegerField(null=True, blank=True)),
                ('language', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'project_sublink',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTargetuser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=80)),
                ('next_cursor', models.BigIntegerField(null=True, blank=True)),
                ('followers_count', models.IntegerField(null=True, blank=True)),
                ('is_active', models.IntegerField()),
                ('date_extraction_end', models.DateTimeField(null=True, blank=True)),
                ('num_consecutive_pages_without_enough_new_followers', models.IntegerField(null=True, blank=True)),
                ('date_last_extraction', models.DateTimeField(null=True, blank=True)),
                ('is_suspended', models.IntegerField()),
            ],
            options={
                'db_table': 'project_targetuser',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTugroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'project_tugroup',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTugroupProjects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_tugroup_projects',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTugroupTargetUsers',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_tugroup_target_users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTweet',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('sent_ok', models.IntegerField()),
                ('sending', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_sent', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'project_tweet',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTweetcheckingmention',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('mentioning_works', models.IntegerField()),
                ('destination_bot_is_checking_mention', models.IntegerField()),
                ('destination_bot_checked_mention', models.IntegerField()),
                ('destination_bot_checked_mention_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'project_tweetcheckingmention',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTweetfromfeed',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_tweetfromfeed',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTweetimg',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('img', models.CharField(max_length=100, blank=True)),
                ('is_using', models.IntegerField()),
            ],
            options={
                'db_table': 'project_tweetimg',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTweetMentionedBots',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_tweet_mentioned_bots',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTweetMentionedUsers',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'project_tweet_mentioned_users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTweetmsg',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=101)),
                ('language', models.CharField(max_length=2, blank=True)),
            ],
            options={
                'db_table': 'project_tweetmsg',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTwitterbotfollowing',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('performed_follow', models.IntegerField()),
                ('followed_ok', models.IntegerField()),
                ('date_followed', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'project_twitterbotfollowing',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTwitteruser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('source', models.IntegerField()),
                ('username', models.CharField(max_length=160)),
                ('twitter_id', models.BigIntegerField()),
                ('country', models.CharField(max_length=2, blank=True)),
                ('language', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=80, blank=True)),
                ('created_date', models.DateTimeField()),
                ('full_name', models.CharField(max_length=160, blank=True)),
                ('geo_enabled', models.IntegerField()),
                ('time_zone', models.CharField(max_length=50, blank=True)),
                ('last_tweet_date', models.DateTimeField(null=True, blank=True)),
                ('followers_count', models.IntegerField(null=True, blank=True)),
                ('tweets_count', models.IntegerField(null=True, blank=True)),
                ('verified', models.IntegerField()),
                ('date_saved', models.DateTimeField()),
            ],
            options={
                'db_table': 'project_twitteruser',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTwitteruserhashashtag',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date_saved', models.DateTimeField()),
            ],
            options={
                'db_table': 'project_twitteruserhashashtag',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectTwitteruserNew',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('source', models.IntegerField()),
                ('username', models.CharField(max_length=160)),
                ('twitter_id', models.BigIntegerField()),
                ('country', models.CharField(max_length=2, blank=True)),
                ('language', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=80, blank=True)),
                ('created_date', models.DateTimeField()),
                ('full_name', models.CharField(max_length=160, blank=True)),
                ('geo_enabled', models.IntegerField()),
                ('time_zone', models.CharField(max_length=50, blank=True)),
                ('last_tweet_date', models.DateTimeField(null=True, blank=True)),
                ('followers_count', models.IntegerField(null=True, blank=True)),
                ('tweets_count', models.IntegerField(null=True, blank=True)),
                ('verified', models.IntegerField()),
                ('date_saved', models.DateTimeField()),
            ],
            options={
                'db_table': 'project_twitteruser_new',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectViewTwitterUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('source', models.IntegerField()),
                ('username', models.CharField(max_length=160)),
                ('twitter_id', models.BigIntegerField()),
                ('country', models.CharField(max_length=2, blank=True)),
                ('language', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=80, blank=True)),
                ('created_date', models.DateTimeField()),
                ('full_name', models.CharField(max_length=160, blank=True)),
                ('geo_enabled', models.IntegerField()),
                ('time_zone', models.CharField(max_length=50, blank=True)),
                ('last_tweet_date', models.DateTimeField(null=True, blank=True)),
                ('followers_count', models.IntegerField(null=True, blank=True)),
                ('tweets_count', models.IntegerField(null=True, blank=True)),
                ('verified', models.IntegerField()),
                ('date_saved', models.DateTimeField()),
                ('project_id', models.IntegerField()),
            ],
            options={
                'db_table': 'project_view_twitter_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SouthMigrationhistory',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app_name', models.CharField(max_length=255)),
                ('migration', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'south_migrationhistory',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
