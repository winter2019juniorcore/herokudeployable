from django.urls import path, include

from django.contrib import admin
from django.conf.urls import url, include
admin.autodiscover()

import hello

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
     path("", hello.views.index, name="index"),
     path("db/", hello.views.db, name="db"),
    # path("admin/", admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url('', include('django_mako_plus.urls')),
]
