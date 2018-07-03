from django.conf.urls import url, include



urlpatterns = [
        url(r'^data/', include('apps.data.api.urls')),
    ]