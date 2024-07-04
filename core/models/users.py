from django.db import models



class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    uid = models.CharField(unique=True, null=True, max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.username
    
    
