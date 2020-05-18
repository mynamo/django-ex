from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^APP/', include('APP.urls')),
]