from django.conf.urls import patterns, include, url

urlpatterns = patterns('phiauth.views',
    url(r'^login/$', 'signIn'),
    url(r'^logout/$', 'signOut'),
    url(r'^profile/$', 'profile'),
)
