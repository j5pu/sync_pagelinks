from django.contrib import admin

from twitter_bots_prod.models import (
    ProjectPagelink,
    ProjectProject,
    ProjectTweetimg,
)


class PagelinkAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'is_active',
    )

    search_fields = (
        'id',
        'page_title',
        'page_link'
    )

    list_filter = (
        'project',
    )

admin.site.register(ProjectPagelink, PagelinkAdmin)
admin.site.register(ProjectProject)
admin.site.register(ProjectTweetimg)