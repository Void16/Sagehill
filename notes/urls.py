from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name='notes_view'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]