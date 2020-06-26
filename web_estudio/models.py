from django.db import models

from django.contrib.auth.models import User

class Turno(models.Model):  
    fecha = models.DateTimeField(auto_now_add=False)
    hora = models.TimeField(auto_now_add=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



