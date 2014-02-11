from django.conf.urls import patterns, include, url

urlpatterns = patterns('auth',
    url(r'^login/$', 'views.signIn'),
    url(r'^logout/$', 'views.signOut'),
    url(r'^profile/$', 'views.profile'),
)
