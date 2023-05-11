from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from . import views

router = SimpleRouter()
router.register('openelective', views.OpenElectiveViewSet, basename='openelective')

# nest_router = NestedSimpleRouter(router, 'openelective')
router.register('openelective/<str:pk>/courselist', views.CourseViewSet, basename='courselist')
router.register('openelective/<str:pk>/responses', views.ResponseViewSet, basename='responses')

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(nest_router.urls)),
]
