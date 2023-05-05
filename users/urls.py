from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from .views import login_view, logout_view, check_user




urlpatterns = [
    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('reset/', PasswordResetView.as_view()),
    path('custom-login/', login_view),
    path('custom-logout/', logout_view),
    path('check-user/', check_user),
]
