from django.urls import path
import signing.views as views

app_name = 'signing'

urlpatterns = [
    path('signin/',  views.LoginView.as_view(), name='signin'),
    path('signup/',  views.SignupView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
