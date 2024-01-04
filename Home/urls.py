from django.urls import path
from .views import *


urlpatterns = [
    path('', profile_page, name = "profile_page"),
    path('login/', login_view.as_view(), name = "login_page"),
    path('register/', registration.as_view(), name = "register_page"),
    path('logout/', logout_page, name = "logout_page"),
]
