from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_todo, name='add_todo'),
    path('toggle_completed/<int:todo_id>/', views.toggle_completed, name='toggle_completed'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]

