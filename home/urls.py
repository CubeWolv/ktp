from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactus' ,views.contact ,name='contact'),
    path('privacypolicy' ,views.policy ,name='privacypolicy'),
    path('termsofuse' ,views.termsofuse ,name='termsofuse'),
    path('aboutus', views.about, name='about')
]