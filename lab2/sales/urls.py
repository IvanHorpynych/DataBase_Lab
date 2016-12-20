from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.listView),
    url(r'^init/$', views.initializeDatabase),
    url(r'^remove/(?P<id>[0-9]+)$', views.removeSale),
    url(r'^(?P<id>[0-9]+)$', views.editSale),
    url(r'^add/$', views.addSale),
]