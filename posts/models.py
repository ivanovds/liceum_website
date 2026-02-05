from django.db import models
from django.contrib.auth.models import User


def upload_image(instance, filename):
    """Returns path to image in media directory."""
    return '/'.join(['posts', str(instance.author.id), filename])


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    main_text = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/posts/%i/" % self.id

    def __str__(self):
        return f'{self.id} - {self.author.username}'
