from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('verify/', views.UserRegisterVerifyView.as_view(), name='verify_code'),
    path('login/', views.LoginUserView.as_view(), name='user_login'),
    path('logout/', views.LogoutUserView.as_view(), name='user_logout'),
    path('changepassword/', views.ChangePasswordView.as_view(), name='change_password'),
]
