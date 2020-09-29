from django.urls import path
from . import views

urlpatterns = [
	path('count/', views.count, name='count'),
	path('', views.homepage, name='home'),
	path('', views.About, name='About us') 
    
	

   
]
