from django.contrib import admin
from .models import UniversityUser, Player, Game, Notice, Event, Team

admin.site.register(UniversityUser)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(Team)