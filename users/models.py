from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=25)
    userNumber = models.CharField(max_length=10)
    userEmail = models.EmailField(max_length=25, unique=True)
    userPass = models.CharField(max_length=25)

    def __str__(self):
        return self.userName