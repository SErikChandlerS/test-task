from django.urls import path
from .views.client_create import RegisterUserView


app_name = 'api_v1_urls'

urlpatterns = [
    path('/api/clients/create', RegisterUserView.as_view(), name='register')
]
