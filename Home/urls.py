from django.urls import path
from Home import views

urlpatterns = [
    path("",views.home , name='home'),
    path("my_projects" , views.my_projects , name='my_projects'),
    path("login" , views.loginUser , name='login'),
    path("sign_up" , views.sign_up, name='sign_up'),
    path("logout" , views.logoutUser , name='logout'),
    path("calculator" , views.calc ,name="calc"),
    path("forgot_password" , views.forgot_password ,name="forgot_password")
]
