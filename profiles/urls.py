"""Profile URL Configuration"""


from django.urls import path

from profiles.views import (
    RegisterView,
    login_view,
    logout_view,
    home_view, 
    ProfileView,
    ProfilesView,
    ProfilesDetailView
)

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profiles/', ProfilesView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfilesDetailView.as_view(), name='profiles-detail')
]
