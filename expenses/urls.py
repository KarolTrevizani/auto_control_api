from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import expenseViewSet

router = DefaultRouter()

# router.register(r'', expenseViewSet)

urlpatterns = router.urls
