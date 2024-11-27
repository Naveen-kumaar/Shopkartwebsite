from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.Register,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('collections',views.Collections,name='collections'),
    path('collections/<str:name>',views.CollectionView,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.ProductDetails,name='ProductDetails')
    
]