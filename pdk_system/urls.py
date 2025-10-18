from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='pdk_system/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('form_blank/', views.form_blank, name='form_blank'),
    path('fill_blank/<int:train_id>/', views.fill_blank, name='fill_blank'),
]
