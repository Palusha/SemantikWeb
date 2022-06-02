from django.contrib import admin

from cinema.models import Actor, Cinema, CustomUser, Employee, Food, Movie, Location

admin.site.register(Actor)
admin.site.register(Cinema)
admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Food)
admin.site.register(Movie)
admin.site.register(Location)
