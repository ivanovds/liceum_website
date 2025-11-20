from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    PROFESSION_CHOICES = [('ST', 'Student'), ('TC', 'Teacher')]

    role = models.CharField(
        max_length=120,
        choices=PROFESSION_CHOICES
    )
    class_number = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    date_of_birth = models.DateField()

    bio = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    interesting_facts = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} {self.role}'

    def save(self, **kwargs):
        if self.role == 'ST' and self.class_number is None:
            raise ValidationError("Student must have class_number")
        super().save(**kwargs)