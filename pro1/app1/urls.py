from .views import *
from django.urls import path

urlpatterns = [
    path('', tic_view, name='tic_url'),
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('signup/', signup_view, name='signup_url'),
    path('cpass/', cpass_view, name='cpass_url'),
]
