"""Profile URL Configuration"""


from django.urls import path
from posts.views import NewPostView, PostsView

urlpatterns = [
    path('new_post/', NewPostView.as_view(), name='new_post'),
    path('', PostsView.as_view(), name='posts')
]


