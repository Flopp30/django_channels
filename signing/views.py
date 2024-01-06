from allauth.account.views import (
    LoginView as AuthLoginView,
    SignupView as AuthSignupView,
    ConfirmEmailView as AuthConfirmEmailView,
    EmailView as AuthEmailView,
    PasswordChangeView as AuthPasswordChangeView,
    PasswordSetView as AuthPasswordSetView,
    PasswordResetView as AuthPasswordResetView,
    PasswordResetDoneView as AuthPasswordResetDoneView,
    LogoutView as AuthLogoutView,
)
import signing.forms as forms
from utils.view_mixins import OpenModalMixin


class LoginView(OpenModalMixin, AuthLoginView):
    form_class = forms.LoginForm
    modal_name = "modal_signin"
    template_name = ".signing/login_form.html"


class SignupView(OpenModalMixin, AuthSignupView):
    form_class = forms.SignupForm
    modal_name = "modal_signup"
    template_name = ".signing/register_form.html"


class ConfirmEmailView(AuthConfirmEmailView):
    ...


class EmailView(AuthEmailView):
    form_class = forms.AddEmailForm


class PasswordChangeView(AuthPasswordChangeView):
    form_class = forms.ChangePasswordForm


class PasswordSetView(AuthPasswordSetView):
    form_class = forms.SetPasswordForm


class PasswordResetView(AuthPasswordResetView):
    form_class = forms.ResetPasswordForm


class PasswordResetDoneView(AuthPasswordResetDoneView):
    pass


class LogoutView(OpenModalMixin, AuthLogoutView):
    modal_name = "modal_logout"
    template_name = ".signing/logout_form.html"
