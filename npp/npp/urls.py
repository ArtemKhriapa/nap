from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^$', HomeView, name='home'),  # temporary plug
    url(r'^api/', include('api.urls')),  # all url, who work for REST
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
