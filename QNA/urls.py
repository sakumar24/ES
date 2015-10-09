from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show_all/$',views.show_all, name='show_all'),
    url(r'^course/(?P<course>.+)/$',views.show_course, name='show_course'),

    url(r'^question/(?P<search_text>.+)/$', views.detail, name='detail'),
]