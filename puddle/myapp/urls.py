from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import loginform

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=loginform), name='login'),
    path('logout/', views.log_out, name='logout'),
]