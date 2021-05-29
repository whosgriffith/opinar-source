# Django imports
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
# Local imports
from .forms import SignupForm

class CustomLogin(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('polls')


class CustomSignup(CreateView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('polls')

    def form_valid(self, form):
        valid = super().form_valid(form)

        # Login the user
        login(self.request, self.object)
        return valid