
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post1/', views.post1, name='post1'),
]
