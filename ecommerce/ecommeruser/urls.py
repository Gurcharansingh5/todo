from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('authlogin',views.authlogin,name= 'authlogin'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('register',views.register,name ='register'),
    path('purhcase/<int:id>',views.purchase,name='purchase')

]
