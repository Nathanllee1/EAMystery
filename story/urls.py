from django.urls import path
from . import views

urlpatterns = [
    path('', views.Background, name='background'),
    path('leavelikealittlebitch', views.leave, name='leavelikealittlebitch'),
]