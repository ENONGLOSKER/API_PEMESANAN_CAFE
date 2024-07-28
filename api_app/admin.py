from django.contrib import admin
from .models import Kategori, Menu, Pesanan, ItemPesanan, Pembayaran
from django.utils.safestring import mark_safe

class PembayaranAdmin(admin.ModelAdmin):
    list_display = ('pesanan', 'status', 'nama_pemesan', 'nomor_hp', 'metode', 'display_bukti_transfer')

    def display_bukti_transfer(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.bukti_transfer.url))
    display_bukti_transfer.short_description = 'Bukti Transfer'

from django.contrib import admin
from .models import Kategori, Menu, Pesanan, ItemPesanan, Pembayaran

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_kategori', 'created', 'updated')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'gambar', 'harga', 'kategori', 'tersedia')

@admin.register(Pesanan)
class PesananAdmin(admin.ModelAdmin):
    list_display = ('nomor_meja', 'keterangan', 'created', 'updated')

@admin.register(ItemPesanan)
class ItemPesananAdmin(admin.ModelAdmin):
    list_display = ('pesanan', 'menu', 'jumlah_menu')
admin.site.register(Pembayaran, PembayaranAdmin)

