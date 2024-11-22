from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.Register,name='register'),
    path('collections',views.Collections,name='collections'),
    path('collections/<str:name>',views.CollectionView,name='collections')
    
]