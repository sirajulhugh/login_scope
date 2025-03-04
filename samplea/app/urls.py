from django.urls import path,include
from .import views

urlpatterns = [

    path('register',views.register,name="register"),
    path('add',views.add_details,name='add_details'),
    path('',views.loginpage,name='loginpage'),
    path('log',views.log,name='log'),
    path('adminmod',views.adminmod,name='adminmod'),
    path('usermod/<int:id>',views.usermod,name='usermod'),
    path('lgout',views.lgout,name='lgout'),

]