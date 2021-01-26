from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView

from . import forms
from .tokens import account_activation_token_generator


class UserRegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user_email = form.cleaned_data['email']
        user = form.save()
        # send confirmation email
        token = account_activation_token_generator.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = 'http://127.0.0.1:8000' + reverse(
            'accounts:confirm-email',
            kwargs={'user_id': user_id, 'token': token})
        message = get_template(
            'registration/account_activation_email.html'
        ).render({'confirm_url': url})
        mail = EmailMessage(
            'CodingPride Account Confirmation',
            message,
            to=[user_email],
            from_email='noreply@codingpride.com')
        mail.content_subtype = 'html'
        mail.send()
        return super().form_valid(form)
