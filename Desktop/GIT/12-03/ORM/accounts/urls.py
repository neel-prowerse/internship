from django.urls import path
from app import views as appviews
from accounts import views
urlpatterns =   [   
                    path('',appviews.home,name='home'),
                    path('signupaccount/',views.signupaccount,name='signupaccount'),
                    path('login/',views.loginaccount,name='loginaccount'),
                    path('logout/',views.logoutaccount,name='logoutaccount'),
                ]