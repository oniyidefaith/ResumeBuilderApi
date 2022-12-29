from django.urls import path, re_path, include, reverse_lazy
from .views import *


urlpatterns = [
    path('register', RegisterApiView.as_view(), name="register"),
    path('login', LoginApiView.as_view(), name="login"),
    path('user', AuthUserApiView.as_view(), name="user"),

]
