from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KategoriViewSet, HPViewSet, PenjualanViewSet

router = DefaultRouter()
router.register(r'kategori', KategoriViewSet)
router.register(r'hp', HPViewSet)
router.register(r'penjualan', PenjualanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
