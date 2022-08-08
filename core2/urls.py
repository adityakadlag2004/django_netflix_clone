
from django.urls import path, include
from .views import Home, ProfileList
urlpatterns = [
    path('', Home.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list'),
]
