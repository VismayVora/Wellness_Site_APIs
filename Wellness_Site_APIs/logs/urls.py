from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from logs import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'dietlogs', views.DietLogViewSet)
router.register(r'workoutlogs', views.WorkoutLogViewSet)


urlpatterns = [
    url('', include(router.urls)),
    #path('healthdata/',views.HealthDataAPIView.as_view({'get': 'list','post':'create','patch':'partial_update','delete':'destroy'}),name='Your health data'),
]