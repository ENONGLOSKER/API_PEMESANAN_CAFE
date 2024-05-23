from django.contrib import admin
from .models import Kategori, Menu, Pesanan, ItemPesanan, Pembayaran

admin.site.register(Kategori)
admin.site.register(Menu)
admin.site.register(Pesanan)
admin.site.register(ItemPesanan)
admin.site.register(Pembayaran)

