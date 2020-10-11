from django.db import models

# Create your models here.
class Todo (models.Model):
    name= models.CharField(max_length=70)
    detail=models.TextField(max_length=500)
    active =models.BooleanField(default=True)



    def __str__(self):
        return self.name
