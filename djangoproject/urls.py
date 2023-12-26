from django.conf.urls import include, url
from django.contrib import admin
from djangoapp.views import home, computer_entry, computer_list

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^computer_entry/$', computer_entry, name='computer_entry'),
    url(r'^computer_list/$', computer_list, name='computer_list'),
]
