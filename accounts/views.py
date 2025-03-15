from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm, UserChangeForm, ChangePasswordForm
import random
from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('accounts:verify_code')
        return render(request, self.template_name, {'form': form})


class UserRegisterVerifyView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = VerifyCodeForm
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                         user_session['full_name'], user_session['password'])

                code_instance.delete()
                messages.success(request, 'you registered.', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'this code is wrong', 'danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')


class LoginUserView(View):
    form_class = UserLoginForm

    # def setup(self, request, *args, **kwargs):
    #     self.next = request.GET.get('next', None)
    #     return super().setup(request, *args, **kwargs)
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('home:home')
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = self. form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'شما وارد حساب خود شدید', 'success')
                return redirect('home:home')
            messages.error(request,  'شما ثبت نام نکرده اید!', 'error')
        return render(request, 'accounts/login.html', {'form': form})


class LogoutUserView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'شما از حساب کاربری خود خارج شدید!', 'success')
        return redirect('home:home')


class ChangePasswordView(View):
    form_class = ChangePasswordForm
    template_name = 'accounts/change_password.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone_number = cd.get('phone_number')
            current_password = cd.get('password')
            new_password = form.cleaned_data.get('new_password')
            new_password_confirm = form.cleaned_data.get('new_password_confirm')
            try:
                user = User.objects.get(phone_number=phone_number)

                if user.check_password(current_password):  # Check if the current password is correct
                    if new_password == new_password_confirm:
                        user.set_password(new_password)
                        user.save()
                        return HttpResponse("Password changed successfully")
                    else:
                        return HttpResponse("New passwords do not match")
                else:
                    return HttpResponse("Incorrect current password")

            except User.DoesNotExist:
                return HttpResponse("User not found")

        return render(request, self.template_name, {'form': form})
