from django.urls import include, path
from . import views

urlpatterns = [
    path('blogs', views.get_blogs)
]
