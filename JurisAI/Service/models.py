from django.db import models
from datetime import date

# Create your models here.

class Client(models.Model):
    username = models.CharField(max_length=122)
    signup_date = models.DateField()
    subscription = models.BooleanField(default=False)
    free_tries = models.IntegerField(default=50)

    def __str__(self):
        return self.username

    @classmethod
    def create_user(cls, username, signup_date=None):
        if signup_date is None:
            signup_date = date.today()
        return cls.objects.create(username=username, signup_date=signup_date)