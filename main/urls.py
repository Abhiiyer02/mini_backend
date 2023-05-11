from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from . import views

router = SimpleRouter()
router.register('openelective', views.OpenElectiveViewSet, basename='openelective')

nest_router = NestedSimpleRouter(router, 'openelective')
nest_router.register('courselist', views.CourseViewSet, basename='courselist')
nest_router.register('responses', views.ResponseViewSet, basename='responses')

urlpatterns = [
    
]
