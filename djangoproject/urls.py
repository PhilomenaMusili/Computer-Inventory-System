from django.conf.urls import include, url
from django.contrib import admin
from djangoapp.views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'djangoapp.views.home', name='home'),
]
