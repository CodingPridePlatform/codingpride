from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.core.mail import EmailMessage
from django.db.models import Q
from django.template.loader import get_template
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


from .models import *
from .tokens import account_activation_token_generator

User = get_user_model()


from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin




class UserCreationForm(forms.ModelForm):
    """A form for creating new users.

    Includes all the required fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def send_confirmation_email(self, user, user_email):
        token = account_activation_token_generator.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = settings.BASE_URL + reverse(
            'accounts:confirm_email',
            kwargs={'user_id': user_id, 'token': token})
        message = get_template(
            'registration/account_activation_email.html'
        ).render({'confirm_url': url})
        mail = EmailMessage(
            'CodingPride Account Confirmation',
            message,
            to=[user_email],
            from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.send()


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email','password1', 'password2']



class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_superuser', )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['email', 'password']



# class UserLoginForm(forms.Form):
#     query = forms.CharField(label = 'Email')
#     password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

#     def clean(self, *args, **kwargs):
#         query = self.cleaned_data.get('query')
#         password = self.cleaned_data.get('password')
#         user_qs_final = User.objects.filter(
#             Q(email__iexact=query)
#         ).distinct()
#         if not user_qs_final.exists() and user_qs_final.count != 1:
#             raise forms.ValidationError("Invalid Credentials provided!")
#         user_obj = user_qs_final.first()
#         if not user_obj.check_password(password):
#             raise forms.ValidationError("Credentials are not correct!")
#         self.cleaned_data["user_obj"] = user_obj
#         return super(UserLoginForm, self).clean(*args, **kwargs)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'is_active', 'is_superuser', )

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
