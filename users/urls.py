from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'users'

# from .views import UserViewSet

router = DefaultRouter()

# router.register(r'', UserViewSet)

urlpatterns = router.urls