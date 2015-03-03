from django.db import models
# Create your models here.


class Post(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    post_id = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    link = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    description = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    image = models.URLField(null=True, blank=True)
    hashtag = models.CharField(max_length=200, null=True, blank=True, db_index=True)


class PagelinkPost(models.Model):
    pagelink_id = models.CharField(max_length=50, null=True, blank=True, db_index=True, default=None)
    post_id = models.CharField(max_length=50, null=True, blank=True, db_index=True)
