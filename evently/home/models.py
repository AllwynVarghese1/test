from django.db import models
import uuid

class Category(models.Model):
    category_name = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.category_name

class Country(models.Model):
    country = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.country


class State(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    state = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.state

class City(models.Model):
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE)
    city = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.city



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    country = models.ForeignKey(
        Country, null=False, blank=False, on_delete=models.CASCADE)
    state = models.ForeignKey(
        State, null=False, blank=False, on_delete=models.CASCADE)
    city = models.ForeignKey(
        City, null=False, blank=False, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    category = models.ForeignKey(
       Category, null=True, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    #featured_image = models.ImageField(
        #null=True, blank=True, default="default.jpg")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

# Create your models here.
