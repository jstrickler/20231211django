from django.contrib import admin
# Register your models here.

from models import Band, Genre, Member

for model in Band, Member:
    admin.site.register(model)

class GenreCustomAdmin(admin.ModelAdmin):
    search_fields = ['name']
