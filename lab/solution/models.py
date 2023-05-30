from django.db import models
from datetime import date

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=2048)
    context = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateField()


