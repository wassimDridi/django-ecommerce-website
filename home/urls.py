from django.urls import path   #,include
#from django.conf.urls import url
from . import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

]