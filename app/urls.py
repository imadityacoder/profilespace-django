from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),

    path('accounts/login/', views.login, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/logout/', views.logout, name='logout'),

    path('<str:username>/', views.user, name='user'),
    path('<str:username>/new/', views.create, name='create'),

    path('<str:username>/page-<pk>/', views.user, name='user'),
    path('<str:username>/page-<pk>/edit/', views.update, name='update'),

]