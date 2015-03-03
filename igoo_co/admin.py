from django.contrib import admin

from igoo_co.models import (
    RedirectPage,
    RedirectPagealias,
    RedirectRedirection,
)


class RedirectAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'uri',
        'card_type',
        'card_img_url',
        'card_description',
    )

    search_fields = (
        'id',
        'card_title',
        'all',
        'card_type',
    )

admin.site.register(RedirectPage, RedirectAdmin)
admin.site.register(RedirectPagealias)
admin.site.register(RedirectRedirection)