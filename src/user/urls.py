from django.urls import path, include
from user.views import UserLoginView
from user.views import UserRegistrationView
from user.views import UserLogoutView


urlpatterns = [
    path('user/register/', UserRegistrationView.as_view(),name='user-registration'),
    path('user/login', UserLoginView.as_view(), name='user-login'),
    path('user/logout', UserLogoutView.as_view(), name='logout'),
]