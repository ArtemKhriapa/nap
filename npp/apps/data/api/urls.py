from django.conf.urls import url

from .views import DataView

urlpatterns = [
        url(r'^$', DataView.as_view()),
    ]