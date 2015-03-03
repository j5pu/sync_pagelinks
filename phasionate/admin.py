from django.contrib import admin

from phasionate.models import (
    # WpAuditTrail,
    # WpCommentmeta,
    # WpComments,
    # WpDuplicatorPackages,
    # WpLinks,
    # WpMymailActions,
    # WpMymailLinks,
    # WpMymailLists,
    # WpMymailListsSubscribers,
    # WpMymailQueue,
    # WpMymailSubscriberFields,
    # WpMymailSubscriberMeta,
    # WpMymailSubscribers,
    # WpNxsLog,
    # WpOptions,
    # WpPostmeta,
    WpPosts,
    # WpRevsliderCss,
    # WpRevsliderLayerAnimations,
    # WpRevsliderSettings,
    # WpRevsliderSliders,
    # WpRevsliderSlides,
    # WpRevsliderStaticSlides,
    # WpRtRtmActivity,
    # WpRtRtmApi,
    # WpRtRtmMedia,
    # WpRtRtmMediaInteraction,
    # WpRtRtmMediaMeta,
    # WpSignups,
    # WpTaxonomymeta,
    # WpTermRelationships,
    # WpTermTaxonomy,
    # WpTerms,
    # WpUsermeta,
    # WpUsers,
    # WpWfbadleechers,
    # WpWfblocks,
    # WpWfblocksadv,
    # WpWfconfig,
    # WpWfcrawlers,
    # WpWffilemods,
    # WpWfhits,
    # WpWfhoover,
    # WpWfissues,
    # WpWfleechers,
    # WpWflockedout,
    # WpWflocs,
    # WpWflogins,
    # WpWfnet404S,
    # WpWfreversecache,
    # WpWfscanners,
    # WpWfstatus,
    # WpWfthrottlelog,
    # WpWfvulnscanners,
)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'post_type',
        'post_date',
        'post_status',
    )

    search_fields = (
        'post_title',
        'id',
        'post_parent'
    )

    list_filter = (
        'post_date',
        'post_status',
        'post_author',
        'post_type',
    )

admin.site.register(WpPosts, PostAdmin)
