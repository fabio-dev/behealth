from django.conf.urls import url
from . import views

app_name = 'calculation'
urlpatterns = [
    # /calculation
    url(r'^$', views.BMIFormView, name='index'),
    # /calculation/bmi
    url(r'^bmi/$', views.BMIFormView, name='bmi'),
    # /calculation/eer
    url(r'^eer/$', views.EERFormView, name='eer'),
]