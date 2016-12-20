from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.listView),
    url(r'^init/$', views.initializeDatabase),
    url(r'^remove/(?P<id>[0-9]+)$', views.removeSale),
    url(r'^(?P<id>[0-9]+)$', views.editSale),
    url(r'^add/$', views.addSale),
    url(r'^setEventTime',views.setTime),
    url(r'^enableTrigger',views.triggerOn),
    url(r'^disableTrigger',views.triggerOff)

    # url(r'^add/$', ''),
    # url(r'^list/remove/(?P<id_of_sale>[0-9]+)/$', ''),
    # url(r'^list/change/(?P<id_of_sale>[0-9]+)/$', ''),
    # url(r'^list/search/text/$', ''),
    # url(r'^list/search/price/$', ''),
    # url(r'^list/search/contains/$', ''),
]