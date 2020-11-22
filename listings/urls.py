from django.urls import path
from .views import index,listing_detail,search

app_name='listings'

urlpatterns = [
    path('',index,name='listings'),
    path('<int:pk>/',listing_detail,name='listing_detail'),
    path('search/',search,name='search'),

]