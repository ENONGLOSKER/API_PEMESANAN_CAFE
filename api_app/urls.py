from django.urls import path
from .views import (
    kategori_list, kategori_detail,
    menu_list, menu_detail,
    pesanan_list, pesanan_detail,
    pembayaran_list, pembayaran_detail
)

urlpatterns = [
    path('kategori/', kategori_list, name='kategori_list'),
    path('kategori/<int:pk>/', kategori_detail, name='kategori_detail'),
    path('menu/', menu_list, name='menu_list'),
    path('menu/<int:pk>/', menu_detail, name='menu_detail'),
    path('pesanan/', pesanan_list, name='pesanan_list'),
    path('pesanan/<int:pk>/', pesanan_detail, name='pesanan_detail'),
    path('pembayaran/', pembayaran_list, name='pembayaran_list'),
    path('pembayaran/<int:pk>/', pembayaran_detail, name='pembayaran_detail'),
]
