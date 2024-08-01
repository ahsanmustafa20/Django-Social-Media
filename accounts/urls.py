from django.urls import path
from django.contrib.auth import views as auth_view # for login and logout view
from . import views

app_name ='accounts'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name= 'logout'),# have a default view and move to home page
    path('signup/', views.SignUp.as_view(), name='signup'),
]
