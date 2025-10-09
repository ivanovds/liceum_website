from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    PROFESSION_CHOICES = [('ST','Student'),('TC','Teacher')]

    role = models.CharField(
        max_length=120,
        choices=PROFESSION_CHOICES
    )
    class_field = models.IntegerField()
    date_of_birth = models.DateField()
    bio = models.TextField(
        max_length=500,
    )
    hobbies = models.TextField(
        blank=True,
        null=True
    )
    interesting_facts = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
