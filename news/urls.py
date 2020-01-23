from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('scrape/', views.scrape, name="scrape"),
    path('list/', views.news_list, name="list")
]
