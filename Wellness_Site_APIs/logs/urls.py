from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from logs import views

router = DefaultRouter()
router.register(r'dietlogs', views.DietLogViewSet)
#router.register(r'users', views.AccountViewSet)

urlpatterns = [
    url('', include(router.urls))
]