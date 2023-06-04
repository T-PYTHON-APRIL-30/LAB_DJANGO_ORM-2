from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    descriptions=models.TextField()
    content=models.TextField()
    raing=models.FloatField()
    models.BooleanField(default=False)
    publish_date=models.DateTimeField(auto_now_add=True)


    
'''''''''''   
def __str__(self):
    return self.title

class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=False)

    def __str__(self):
        return self.title
'''''
