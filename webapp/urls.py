

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


urlpatterns = patterns('webapp.pages',
                       url(r'^$', 'homepage'),
                       url(r'^profile/(\d+)/$', 'user_profile'),
                       url(r'^Edit_profile/$', 'edit_profile'),
                       url(r'^All_users/$', 'all_users'),
                       url(r'^Wall_post_Page/(\d+)/$', 'wall_post_page'),
                       url(r'^Newsfeed/$', 'newsfeed'),
                       )


urlpatterns += patterns('webapp.form_receivers',
                        url('^__form_receiver/loginform/$', 'login'),
                        url('^__form_receiver/shortsignupform/$', 'sign_up'),
                        url('^__form_receiver/create_wall_post/(\\d+)/$',
                            'create_wall_post'),
                        url('^__form_receiver/edit_user/$', 'edit_user'),
                        )


admin.autodiscover()

urlpatterns += patterns('',
                        url(r'', include("social_auth.urls")),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^grappelli/', include('grappelli.urls')),
                        url(r'^__logout/$', logout, kwargs={'next_page': '/'}),
                        )
