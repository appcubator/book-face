

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


urlpatterns = patterns('webapp.pages',
                       url(r'^$', 'homepage'),
                       )


urlpatterns += patterns('webapp.form_receivers',
                        url('^__form_receiver/loginform/$', 'login'),
                        url('^__form_receiver/shortsignupform/$', 'sign_up'),
                        )


admin.autodiscover()

urlpatterns += patterns('',
                        url(r'', include("social_auth.urls")),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^grappelli/', include('grappelli.urls')),
                        url(r'^__logout/$', logout, kwargs={'next_page': '/'}),
                        )
