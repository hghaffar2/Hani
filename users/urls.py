from django.urls import path
from .views import users


urlpatterns = [

    path('sign-user', users.signup, name='sign'),
    path('login-user', users.user_login, name='CustomLogin'),
    path('profile', users.listing, name='listing'),
    path('addImage/', users.addImg, name='addImg'),
    path('submitImage/', users.submitImg, name='subImg'),



]




