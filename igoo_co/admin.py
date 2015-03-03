from django.contrib import admin

from igoo_co.models import (
    RedirectPage,
)


class RedirectAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'uri',
        'card_title',
        'card_img_url'
    )

    search_fields = (
        'id',
        'card_title',
        'all'
    )

admin.site.register(RedirectPage, RedirectAdmin)