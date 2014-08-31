from django.conf.urls import patterns, include, url
from rest_framework import routers
from products import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
)