from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import *

app_name = "accounts"
urlpatterns = [
    path('test/', TestView.as_view({'get': 'test'}), name='test'),
    path('auth/', obtain_jwt_token)
]
