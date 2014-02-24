from django.conf.urls import patterns, include, url

urlpatterns = patterns('cms.views',
    url(r'^$', 'home'),
    url(r'^display/(?P<user_login>\w+)/(?P<id_doc>\d+)/$', 'display'),
    url(r'create/$', 'create'),
)
