from django.urls import path
from account.views import CustomUserCreate

app_name = 'account'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create-user'),
]