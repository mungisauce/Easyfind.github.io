
"""
URL configuration for easyfind project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from Attendance import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('base/',views.base,name='base'),
    path('attendance_records/',views.attendance_records,name='attendance_records'),
    path('mark_attendance/',views.mark_attendance,name='mark_attendance'),
    path('worker_list/',views.worker_list,name='worker_list'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact, name='contact'),
    path('login_view/',views.login_view,name='login_view'),
    path('signup/',views.signup,name='signup'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')

]