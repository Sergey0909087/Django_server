from django.urls import include, path,  re_path
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'titls', views.BlogViewSet)


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^titles/(?P<id>\d+)', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]