from django.contrib import admin
from .models import MovieData, MovieViewer, WatchList
# Register your models here.

admin.site.register(MovieData)
admin.site.register(MovieViewer)
admin.site.register(WatchList)
