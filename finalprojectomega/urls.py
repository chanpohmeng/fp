from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cpmeye/', include('cpmeye.urls')),        
#    url(r'^add_submission/$', include('cpmeye.urls')), # NEW MAPPING!
#    url(r'^register/$', include('cpmeye.urls')),
#    url(r'^suggest_submission/$', include('cpmeye.urls')),
#    url(r'^login/$', include('cpmeye.urls')),
#    url(r'^logout/$', include('cpmeye.urls')),
)
