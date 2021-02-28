
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, View

from .forms import *
from .models import Profile
from .tokens import account_activation_token_generator

User = get_user_model()

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView


class UserRegistrationView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user_email = form.cleaned_data['email']
        user = form.save()
        # send confirmation email
        form.send_confirmation_email(user, user_email)

        messages.success(self.request,
                         'Please check your email for confimation.')
        return super().form_valid(form)


class ConfirmRegistrationView(View):
    """View for user to confirm registration."""

    def get(self, request, user_id, token):
        user_id = force_str(urlsafe_base64_decode(user_id))

        user = User.objects.get(pk=user_id)

        if user and account_activation_token_generator.check_token(
                user, token):
            user.is_active = True
            user.save()
            messages.success(
                request, ('Registration completed successful. '
                          'Please login to continue..'))

        return redirect('accounts:login')


# def loginView(request, *args, **kwargs):
#     form = UserLoginForm()
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST or None)
#         if form.is_valid():
#             user_obj = form.cleaned_data.get('user_obj')
#             login(request, user_obj)
#             return HttpResponseRedirect('/')
#     myTemplate = 'registration/login.html'
#     context = {
#         'form': form
#     }
#     return render(request, myTemplate, context)

def login_url(request):
    send_url = request.GET.get('send_url')
    print('send_url:', send_url)
    return send_url


class loginView(BSModalLoginView):
    authentication_form = UserLoginForm
    template_name = 'registration/login.html'
    # success_message = 'Success: You were successfully logged in.'
    extra_context = dict(next=reverse_lazy('question:qn-create'))
    
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        red_url = login_url(self.request)
        print('red_url:', red_url)
        # context.update({
        #     self.redirect_field_name: self.get_redirect_url(),
        #     'site': current_site,
        #     'site_name': current_site.name,
        #     **(self.extra_context or {})
        # })
        return context



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'registration/profile.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
