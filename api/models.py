from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    class Meta:
        db_table = 'user'    
