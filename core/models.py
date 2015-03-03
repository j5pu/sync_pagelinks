from django.db import models
# Create your models here.


class PagelinkPost(models.Model):
    pagelink_id = models.CharField(max_length=50, null=True, blank=True, db_index=True, default=None)
    post_id = models.CharField(max_length=50, null=True, blank=True, db_index=True)
