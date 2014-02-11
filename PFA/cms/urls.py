from django.conf.urls import patterns, include, url

urlpatterns = patterns('cms',
    url(r'^index/$', 'views.cms_index'),
)
