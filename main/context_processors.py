from allauth.account.forms import LoginForm, SignupForm


def user_forms_context_processor(request):
    return {
        'signup_form': SignupForm(),
        'signin_form': LoginForm()
    }
