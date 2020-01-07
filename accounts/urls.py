from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# django project might have multiple of apps so in order to differtiate between
# them and tell django which url and view to encounter we need to set our
# application namespace

app_name = 'accounts'

urlpatterns = [
	path('signup/', views.signup , name='signup'),
	path('login/', auth_views.LoginView.as_view(template_name = 'auth/login.html'),
         name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]