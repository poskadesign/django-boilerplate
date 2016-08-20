from django.conf.urls import url, include
from django.contrib import admin

import usecase.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
