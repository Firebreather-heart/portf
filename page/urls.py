from django.urls import path
from .views import index,messageme,register

urlpatterns = [ 
    path('',index,name='home'),
    path('msg/', messageme, name='dm'),
    path('register/',register, name='register'),
]