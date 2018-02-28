from django.contrib import admin
from api.models import (
    TeamPermissions,
    Organization,
    Team
)


class TeamPermissionsInline(admin.TabularInline):
    model = TeamPermissions
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inline = [
        TeamPermissionsInline
    ]


admin.register(Organization)
