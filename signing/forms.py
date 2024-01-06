from allauth.account.forms import (
    LoginForm as AuthLoginForm,
    SignupForm as AuthSignupForm,
    AddEmailForm as AuthAddEmailForm,
    ChangePasswordForm as AuthChangePasswordForm,
    SetPasswordForm as AuthSetPasswordForm,
    ResetPasswordForm as AuthResetPasswordForm,
)


class LoginForm(AuthLoginForm):

    def login(self, *args, **kwargs):
        # implement specific logic here
        return super().login(*args, **kwargs)


class SignupForm(AuthSignupForm):

    def save(self, request):
        user = super().save(request)
        return user


class AddEmailForm(AuthAddEmailForm):

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns an allauth.account.models.EmailAddress object.
        email_address_obj = super().save(request)
        # Add your own processing here.
        # You must return the original result.
        return email_address_obj


class ChangePasswordForm(AuthChangePasswordForm):

    def save(self):
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super().save()

        # Add your own processing here.


class SetPasswordForm(AuthSetPasswordForm):

    def save(self):
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super().save()

        # Add your own processing here.


class ResetPasswordForm(AuthResetPasswordForm):

    def save(self, request, commit=True):
        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super().save(request, commit)

        # Add your own processing here.

        # Ensure you return the original result
        return email_address
