from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('signup/', views.login, name='login'),
    path('login/', views.signup, name='signup'),

    path('<slug:slug>/', views.user, name='user'),
    path('<slug:slug>/new/', views.create, name='create'),

    path('<slug:slug>/<slug:page>', views.user, name='user'),
    path('<slug:slug>/<slug:page>/edit/', views.update, name='update'),
    path('<slug:slug>/<slug:page>/delete/', views.delete, name='delete'),

]