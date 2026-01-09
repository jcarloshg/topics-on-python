from django.urls import path
from .views import RegisterView, LoginView, RefreshTokenView

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh-token/', RefreshTokenView.as_view(), name='token_refresh'),
]
