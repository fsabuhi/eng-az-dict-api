from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('getword/<str:word>/', views.getword, name='getword')
]               