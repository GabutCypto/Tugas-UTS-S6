from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HPViewSet, HP1JutaanViewSet, HP2JutaanViewSet

router = DefaultRouter()
router.register(r'hp', HPViewSet)
router.register(r'hp1jutaan', HP1JutaanViewSet)
router.register(r'hp2jutaan', HP2JutaanViewSet)

urlpatterns = router.urls
