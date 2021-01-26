from django.views.generic import CreateView

from . import forms


class UserRegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user_email = form.cleaned_data['email']
        # send confirmation email
        return super().form_valid(form)
