"""Profile URL Configuration"""


from django.urls import path
from posts.views import NewPostView, PostsView, PostsDetailedView

urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
    path('new_post/', NewPostView.as_view(), name='new_post'),
    path('<int:pk>/', PostsDetailedView.as_view(), name='posts-detail')
]


