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

    def to_representation(self, instance): 
        representation = super().to_representation(instance)
        if instance.gambar:
            request = self.context.get('request')
            representation['gambar'] = request.build_absolute_uri(f'/static{instance.gambar.url}')
        return representation

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
    
    def validate(self, data):
        if data['metode'] == 'transfer' and 'bukti_transfer' not in data:
            raise serializers.ValidationError("Bukti pembayaran diperlukan untuk metode transfer.")
        if data['metode'] == 'cash' and 'bukti_transfer' in data:
            raise serializers.ValidationError("Bukti pembayaran tidak perlu disediakan untuk metode cas/tunai.")
        return data