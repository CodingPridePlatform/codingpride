from . import forms


def user_forms_context(request):
    return {
        'signin_form': forms.UserLoginForm(),
        'signup_form': forms.UserCreationForm(),
    }
