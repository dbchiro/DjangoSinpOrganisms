from django.contrib import admin
from django.utils.translation import gettext as _

# Register your models here.
from .models import Organism, OrganismMember


@admin.action(description=_("Mark selected items as active"))
def activate(_modeladmin, _request, queryset):
    """Set item active"""
    queryset.update(enabled=True)


@admin.action(description=_("Mark selected items as inactive"))
def inactivate(_modeladmin, _request, queryset):
    """Set item inactive"""
    queryset.update(enabled=False)


class OrganismAdmin(admin.ModelAdmin):
    """Organism admin viewset"""

    list_display = (
        "id",
        "short_label",
        "status",
        "type",
        "action_scope",
        "enabled",
        "parent",
    )
    list_filter = ("type", "enabled", "geographic_area")
    actions = [activate, inactivate]


class OrganismMemberAdmin(admin.ModelAdmin):
    """Organism members admin viewset"""

    list_display = (
        "member",
        "organism",
        "member_level",
    )
    list_filter = ("organism", "member_level")


admin.site.register(Organism, OrganismAdmin)
admin.site.register(OrganismMember, OrganismMemberAdmin)
