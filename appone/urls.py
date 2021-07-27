from django.urls import  path
from . import  views

urlpatterns=[
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('booking/',views.booking,name='booking'),
    path('booking_save/',views.booking_save,name='booking_save'),
    path('contact_save/',views.contact_save,name='contact_save'),
    path('about/',views.about,name='about'),
    path('feature/',views.feature,name='feature'),
    path('team/',views.team,name='team'),
    path('menu/',views.menu,name='menu'),
    path('index/',views.index,name='index')

]