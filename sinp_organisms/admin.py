from django.contrib import admin

# Register your models here.
from .models import Organism, OrganismMember


class OrganismAdmin(admin.ModelAdmin):
    list_display = ("id", "short_label", "status", "type", "action_scope")
    list_filter = ("type",)


class OrganismMemberAdmin(admin.ModelAdmin):
    list_display = (
        "member",
        "organism",
        "member_level",
    )
    list_filter = ("organism", "member_level")


admin.site.register(Organism, OrganismAdmin)
admin.site.register(OrganismMember, OrganismMemberAdmin)
