from django.urls import path
from .views import CustomLoginView, SignUpView, RefreshTokenView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('refresh-token/', RefreshTokenView.as_view(), name='refresh_token'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', CustomLoginView.as_view(), name='home'),
]
