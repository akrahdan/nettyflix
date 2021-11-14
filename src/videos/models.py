from django.db import models
from django.db.models.expressions import F

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    #timestamp
    #updated
    #state
