from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),


    # Get all_blogs for all authenticated Users
    path('blogs/', views.BlogList.as_view()),
    # path('create-blog/', views.Create_Blog.as_view()),
    # path('update-blog/<int:pk>/', views.Update_Blog.as_view()),

    path('blogs/<int:pk>/', views.BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
