from django.conf.urls import include, url
from .import views

urlpatterns = [
        url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
        url(r'^all/$', views.category, name='category_all' )

]
