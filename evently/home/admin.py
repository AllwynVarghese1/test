from django.contrib import admin
from .models import Category, Country, State, City, Event

admin.site.register([Category, Country, State, City, Event])