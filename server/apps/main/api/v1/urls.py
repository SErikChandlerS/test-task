from django.urls import path
from .views.client_create import RegisterUserView
from .views.match import MatchView

app_name = 'api_v1_urls'

urlpatterns = [
    path('clients/create', RegisterUserView.as_view({'post': 'create'}), name='register'),
    path('list/', RegisterUserView.as_view({'get': 'list'}), name='users_list'),
    path('clients/<int:pk>/match', MatchView.as_view({'post': 'match'}), name='create_match'),
]

