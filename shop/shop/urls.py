from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/', include('product.urls', namespace="product" )),
    url(r'^', views.home, name='home'),

]

