from rest_framework import serializers
from .models import Kategori, Menu, Pesanan, ItemPesanan, Pembayaran

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['nama_kategori', 'created', 'updated']

class MenuSerializer(serializers.ModelSerializer):
    kategori = KategoriSerializer()
    
    class Meta:
        model = Menu
        fields = ['id', 'nama', 'gambar', 'harga', 'kategori']

class ItemPesananSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    
    class Meta:
        model = ItemPesanan
        fields = ['menu', 'jumlah_menu']

class PesananSerializer(serializers.ModelSerializer):
    items = ItemPesananSerializer(many=True)
    total_harga = serializers.SerializerMethodField()
    
    class Meta:
        model = Pesanan
        fields = ['nomor_meja', 'items', 'total_harga', 'keterangan', 'created', 'updated']

    def get_total_harga(self, obj):
        return obj.total_harga()

class PembayaranSerializer(serializers.ModelSerializer):
    pesanan = PesananSerializer()
    
    class Meta:
        model = Pembayaran
        fields = ['nama_pemesan', 'pesanan', 'metode', 'bukti_transfer']
