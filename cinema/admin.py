from django.contrib import admin

from cinema.models import Cinema, Actor, Movie, Employee, CustomUser

admin.site.register(Cinema)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Employee)
admin.site.register(CustomUser)
