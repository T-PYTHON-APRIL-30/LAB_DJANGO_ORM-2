from django.db import models

# Create your models here.
class Blog(models.Model):
    Title=models.CharField(max_length=2048)
    Content=models.TextField() 
    is_published= models.BooleanField()
    publish_date= models.DateField()