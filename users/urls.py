from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet

app_name = 'users'

router = DefaultRouter()

router.register(r'register-user', UserViewSet)

urlpatterns = router.urls