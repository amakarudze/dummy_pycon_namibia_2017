from django.conf.urls import url
from dummy_site import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
]