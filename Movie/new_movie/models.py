from django.db import models

# Create your models here.


class movie(models.Model):

        title = models.CharField(max_length=200)
        content = models.TextField()
        is_published = models.BooleanField()
        publish_date = models.DateTimeField()