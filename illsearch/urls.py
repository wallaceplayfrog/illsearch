
from django.conf.urls import url
from . import views

urlpatterns = [

    url('^$', views.main),
    url('^personal/$', views.personal),
    url('^probability', views.probability),
    url('^way$', views.way),


]
