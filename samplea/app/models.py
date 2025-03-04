from django.db import models
from django.contrib.auth.models import User

# Create your models
class Registeration(models.Model):
    age=models.IntegerField(null=True)
    phnoenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=20)    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)