from django.urls import path
from Teacher import views

urlpatterns = [
    path('tt/',views.myteacher),
    
    ]