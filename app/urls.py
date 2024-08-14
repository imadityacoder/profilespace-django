from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

    path('<slug:slug>/', views.user, name='user'),
    path('<slug:slug>/new/', views.create, name='create'),

    path('<slug:slug>/<slug:page>', views.user, name='user'),
    path('<slug:slug>/<slug:page>/edit/', views.update, name='update'),

]