from django.urls import path
from .views.client_create import RegisterUserView
from .views.match import MatchView

app_name = 'api_v1_urls'

urlpatterns = [
    path('/api/clients/create', RegisterUserView.as_view(), name='register'),
    path('/clients/<int:pk>/match', MatchView.as_view({'post': 'match'}), name='create_match'),
]
