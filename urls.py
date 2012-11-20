from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RadioShack.views.home', name='home'),
    # url(r'^RadioShack/', include('RadioShack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #url(r'^$', 'RadioShack.shopping_site.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
