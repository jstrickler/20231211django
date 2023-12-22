from django.contrib import admin
from superheroes.models import Superhero, Power, Enemy, City # import your models

class SuperheroPowersInline(admin.TabularInline):
    model = Superhero.powers.through

class SuperheroEnemiesInline(admin.TabularInline):
    model = Superhero.enemies.through

class EnemyPowersInline(admin.TabularInline):
    model = Enemy.powers.through

class SuperheroInline(admin.TabularInline):
    model = Superhero
    fields = ['name']

# customize the admin
class PowerAdmin(admin.ModelAdmin):  # create custom Admin model
    search_fields = ['name', 'description'] # add Admin metadata
    inlines = [SuperheroPowersInline, EnemyPowersInline]

class SuperHeroAdmin(admin.ModelAdmin):
    search_fields = ['name', 'real_name', 'secret_identity']
    inlines = [SuperheroPowersInline, SuperheroEnemiesInline]
    exclude = ['powers', 'enemies']

class EnemyAdmin(admin.ModelAdmin):
    exclude = ["powers"]
    inlines = [EnemyPowersInline]

class CityAdmin(admin.ModelAdmin):
    inlines = [SuperheroInline]

admin.site.register(Power, PowerAdmin) # register custom model
admin.site.register(Superhero, SuperHeroAdmin)
admin.site.register(Enemy, EnemyAdmin)
admin.site.register(City, CityAdmin)
