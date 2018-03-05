from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^register/$', views.register, name='register'),
        url(r'^register/login/$', views.register2, name='register2'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'login/check', views.check, name='check'),
        url(r'login/profile', views.profile, name='profile'),
    ]
