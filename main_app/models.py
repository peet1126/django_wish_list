from django.db import models
from django.urls import reverse

# Create your models here.
class Wish(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.id})