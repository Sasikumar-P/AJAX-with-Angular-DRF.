from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^author/$',views.author_list),
    url(r'^author/(?P<pk>[0-9]+)/$',views.author_detail),
    
]
