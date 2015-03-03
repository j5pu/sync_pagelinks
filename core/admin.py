from django.contrib import admin

# Register your models here.
from core.models import (
    PagelinkPost,
)


class PagelinkPostAdmin(admin.ModelAdmin):
    list_display = (
        'pagelink_id',
        'post_id',
    )

    search_fields = (
        'post_id',
        'pagelink_id',
    )


admin.site.register(PagelinkPost, PagelinkPostAdmin)
