from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(
            self.request, "Registration successful! You are now logged in.")
        from django.http import HttpResponseRedirect
        # Use explicit HttpResponseRedirect for correct CBV typing
        return HttpResponseRedirect(reverse_lazy('home'))


class RefreshTokenView(TemplateView):
    template_name = 'refresh_token.html'

    def post(self, request, *args, **kwargs):
        # Extend session expiry as SSR "refresh token" concept
        if request.user.is_authenticated:
            request.session.set_expiry(3600)  # Session expires in 1 hour
            messages.success(request, "Session has been refreshed!")
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(reverse_lazy('home'))
