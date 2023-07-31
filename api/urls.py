# url_scrapper/api/urls.py
from django.urls import path
from .views import scrape_url_view
from url_scrapper import views\
    
url = 'http://localhost:8000/api/scrape/'

urlpatterns = [
    path('scrape/', scrape_url_view, name='scrape_url'),
    path('', views.index, name='index'),
]
