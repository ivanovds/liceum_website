"""Profile URL Configuration"""


from django.urls import path
from posts.views import NewPostView

urlpatterns = [
    path('new_post/', NewPostView.as_view(), name='new_post')
]
