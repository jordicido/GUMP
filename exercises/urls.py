from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from exercises import views

router = DefaultRouter()
router.register(r'exercises', views.ExerciseViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]