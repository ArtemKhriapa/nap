from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import HomeView


urlpatterns = [
    url(r'^data/', include('apps.data.api.urls')),

    url(r'^home/', HomeView, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
]