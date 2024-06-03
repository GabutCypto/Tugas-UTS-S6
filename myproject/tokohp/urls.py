from django.urls import path
from . import views

urlpatterns = [
    # URLs for views related to Kategori
    path('kategori/', views.KategoriListCreateView.as_view(), name='kategori-list-create'),
    path('kategori/<int:pk>/', views.KategoriDetailView.as_view(), name='kategori-detail'),

    # URLs for views related to HP
    path('hp/', views.HPListCreateView.as_view(), name='hp-list-create'),
    path('hp/<int:pk>/', views.HPDetailView.as_view(), name='hp-detail'),

    # URLs for views related to Penjualan
    path('penjualan/', views.PenjualanListCreateView.as_view(), name='penjualan-list-create'),
    path('penjualan/<int:pk>/', views.PenjualanDetailView.as_view(), name='penjualan-detail'),
]
