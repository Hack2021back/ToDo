from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from .utils import DataMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


def today(request):
    return render(request, "build/index.html")
def inbox(request):
    return render(request,"build/index.html")

class RegisterUser(DataMixin, SuccessMessageMixin, CreateView):
    """Show register form"""

    form_class = RegisterUserForm
    template_name = "to_do_app/registr/index.html"
    success_url = reverse_lazy("sign_in")
    success_message = "User added successfully"
    error_message = "Registration error"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Registration", ico="menu/img/ico/home_pink.png"
        )
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, SuccessMessageMixin, LoginView):
    """Autorization class"""

    form_class = LoginUserForm
    template_name = "to_do_app/registr/login.html"
    error_message = "Something went wrong"
    success_url = reverse_lazy("home")
    user = ""
    success_message = f"Successfully sign in"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title="Sign in", ico="menu/img/ico/home_pink.png")

        return dict(list(context.items()) + list(c_def.items()))


class LogoutUser(LoginRequiredMixin, LogoutView, SuccessMessageMixin):
    next_page = "home"
    success_message = "Logout successfully"
