""" Main project url confuguration module. Other url modules
    to be included in this module.
"""

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Custom apps' urls
    url(r'^', include('candidates.urls')),
    url(r'^', include('recruiters.urls')),

    # Third party apps' urls
    url(r'^', include('social_auth.urls')),
    url(r'^api', include('rest_framework.urls', namespace='rest_framework')),

    # Admin urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
