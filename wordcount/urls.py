from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    # after views.py we name to create name of function
    # anytime there is nothing after url => views.home
    path('count/', views.count, name='count')
]
