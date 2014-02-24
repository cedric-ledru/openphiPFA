from django.conf.urls import patterns, include, url

urlpatterns = patterns('cms',
    url(r'^$', 'views.home'),
    url(r'create/$', 'views.create'),
)
