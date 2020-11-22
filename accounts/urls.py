from django.urls import path
from .views import login,dashboard,register,logout

app_name='accounts'

urlpatterns=[
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('register/',register,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
]