from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    role = models.TextChoices("student", "teacher")
    grade = models.TextField(max_length=20)
    date_of_birth = models.DateField()
    bio = models.TextField()
    hobbies = models.TextField()
    interesting_facts = models.TextField()
