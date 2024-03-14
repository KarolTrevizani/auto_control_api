from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()

router.register(r'types', TypeViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = router.urls