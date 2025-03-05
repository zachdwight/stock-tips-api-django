from django.urls import path
from . import views 

urlpatterns = [
    path('financial-news/', views.get_financial_news, name='financial-news'),
    
]
