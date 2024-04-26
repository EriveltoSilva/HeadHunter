from . import views 
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path('login/', views.login,name="login"),    
    path('logout/', views.logout,name="logout"),    
    path('registro-particular/', views.signup_personal,name="signup-personal"),    
    path('registro-empresarial/', views.signup_business,name="signup-business"),    
    path('recuperacao-de-palavra-passe/', views.password_reset,name="password-reset"),    
    path('alterar-palavra-passe/', views.password_change,name="password-change"),    
]
