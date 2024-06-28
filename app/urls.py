from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    
    path('<slug:slug>/', views.user, name='user'),
    path('new/', views.create, name='create'),
    path('edit/', views.update, name='update'),

]