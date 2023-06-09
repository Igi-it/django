from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goldline.html', views.goldline, name='goldline'),
    path('automag.html', views.automag, name='automag'),
    path('m249.html', views.m249, name='m249'),
    path('beretta.html', views.beretta, name='beretta'),

]
