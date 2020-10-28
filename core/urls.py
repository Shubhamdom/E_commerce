from django.urls import path
from .views import *
app_name = 'core'
urlpatterns = [
    path('seller/',sellerRegister,name='seller'),
    path('addSellerData/',adminUserInfo,name='addSellerData')
]
