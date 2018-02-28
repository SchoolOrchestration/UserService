from django.contrib import admin
from api.models import (
    TeamPermissions,
    Organization,
    Permission,
    Team,
)

admin.site.register(TeamPermissions)
admin.site.register(Organization)
admin.site.register(Permission)
admin.site.register(Team)
