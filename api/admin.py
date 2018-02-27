from django.contrib import admin
from api.models import (
    Organization,
    Team
)


class TeamInline(admin.TabularInline):
    model = Team
    extra = 1


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [
        TeamInline,
    ]
