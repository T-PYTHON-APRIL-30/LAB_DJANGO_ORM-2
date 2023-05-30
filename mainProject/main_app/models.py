from django.db import models

# Create your models here.

class blog(models.Model):
    title= models.CharField(max_length=15)
    Content=models.TextField()
    is_published= models.BooleanField()
    publish_date=models.DateField()
    
    


