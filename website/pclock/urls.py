from django.conf.urls import patterns, include, url
from django.contrib import admin

import website


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pclock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.index', name="index"),
)
