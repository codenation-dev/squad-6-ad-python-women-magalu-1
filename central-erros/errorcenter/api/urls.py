from django.urls import include, path

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'logs', views.LogApiViewSet)
router.register(r'origins', views.OriginApiViewSet)
router.register(r'users', views.UserApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('environments/', views.EnvironmentListOnlyApiView.as_view())
]

