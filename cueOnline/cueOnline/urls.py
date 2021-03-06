"""cueOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CueApp import views
import django

DEBUG = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('info',views.info),
    path('register',views.register),
    path('registerdone',views.register_done),
    #path('404/', custom_page_not_found),
    path('cuetable',views.cue_table),
    path('addUser',views.addUser),
    path('cue',views.customer_cue),
    path('shopadmin',views.shop_admin),
    path('choosecue',views.shop_choose_cue),
    path('login',views.login),
    path('login_success', views.login_success),
    path('logout',views.logout, name = 'logout'),
    path('requestcueform',views.cue_request_form, name = 'requestcueform'),
    path('add_cue_request',views.add_cue_request),
    path('add_cue_request_done',views.add_cue_request_done),
    #Change Cue
    path('change_cue_a',views.change_cue_a, name = 'change_cue_a'),

    #Choose Cue or Press Cue
    path('press_cue_all',views.press_cue_all, name = 'press_cue_all'),

    #Show Your Cue
    path('your_cue_a',views.your_cue_a, name = 'your_cue_a'),
    path('your_cue_b',views.your_cue_b, name = 'your_cue_b'),
    path('your_cue_c',views.your_cue_c, name = 'your_cue_c'),

    #Change Cue Button action
    path('change_cue_button',views.change_cue_button, name = 'change_cue_button'),



]
