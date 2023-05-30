from django.db import models

class Post(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=2048)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    publish_date = models.DateField()
