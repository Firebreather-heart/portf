from django.urls import path
from .views import index,messageme

urlpatterns = [ 
    path('',index,name='home'),
    path('msg/', messageme, name='dm')
]