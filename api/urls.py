from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageListCreateAPIView.as_view()), 
    path('messages-d/', views.MessageDestroyAPIView.as_view()), 
]