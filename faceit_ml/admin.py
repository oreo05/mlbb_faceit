from django.contrib import admin
from .models import Match, MatchmakingQueue

# Register your models here.
admin.site.register(Match)
admin.site.register(MatchmakingQueue)
