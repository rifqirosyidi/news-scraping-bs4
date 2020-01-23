from django.urls import path
from . import views


app_name = 'notes'
urlpatterns = [
    path('', views.list_notes, name='list',),
    path('create/', views.create_notes, name='create'),
]
