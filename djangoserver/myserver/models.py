from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
# Create your models here.
