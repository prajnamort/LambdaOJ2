from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from main import views


router = routers.DefaultRouter()
router.register(r'problems', views.problem.ProblemViewSet)


urlpatterns = [
    url(r'^$',
        views.index.main_index, name='index'),
    url(r'^api/',
        include(router.urls)),
]
