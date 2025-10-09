from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    role = models.TextChoices("student", "teacher")
    class_ = models.TextField(max_length=20)
    date_of_birth = models.DateField()
    bio = models.TextField(max_length=500)
    hobbies = models.TextField(max_length=100)
    interesting_facts = models.TextField(max_lenght=500)
