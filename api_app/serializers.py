from rest_framework import serializers
from .models import Kategori, Menu, Pesanan, ItemPesanan, Pembayaran

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama_kategori', 'created', 'updated']

class MenuSerializer(serializers.ModelSerializer):
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())
    kategori_detail = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'nama', 'gambar', 'harga', 'kategori', 'kategori_detail']

    def get_kategori_detail(self, obj):
        return KategoriSerializer(obj.kategori).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.gambar:
            request = self.context.get('request')
            representation['gambar'] = request.build_absolute_uri(instance.gambar.url)
        return representation

class ItemPesananSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = ItemPesanan
        fields = ['id', 'menu', 'jumlah_menu']

    def create(self, validated_data):
        menu_data = validated_data.pop('menu')
        menu = Menu.objects.get(id=menu_data['id'])
        item_pesanan = ItemPesanan.objects.create(menu=menu, **validated_data)
        return item_pesanan

class PesananSerializer(serializers.ModelSerializer):
    items = ItemPesananSerializer(many=True)
    total_harga = serializers.SerializerMethodField()

    class Meta:
        model = Pesanan
        fields = ['id', 'nomor_meja', 'keterangan', 'created', 'updated', 'items', 'total_harga']

    def get_total_harga(self, obj):
        return obj.total_harga()

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        pesanan = Pesanan.objects.create(**validated_data)
        for item_data in items_data:
            ItemPesanan.objects.create(pesanan=pesanan, **item_data)
        return pesanan

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.nomor_meja = validated_data.get('nomor_meja', instance.nomor_meja)
        instance.keterangan = validated_data.get('keterangan', instance.keterangan)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        # Update or create items
        for item_data in items_data:
            item_id = item_data.get('id')
            if item_id:
                item = ItemPesanan.objects.get(id=item_id, pesanan=instance)
                item.menu = item_data.get('menu', item.menu)
                item.jumlah_menu = item_data.get('jumlah_menu', item.jumlah_menu)
                item.save()
            else:
                ItemPesanan.objects.create(pesanan=instance, **item_data)
        
        return instance

class PembayaranSerializer(serializers.ModelSerializer):
    pesanan = PesananSerializer()

    class Meta:
        model = Pembayaran
        fields = "__all__"

    def validate(self, data):
        if data['metode'] == 'transfer' and not data.get('bukti_transfer'):
            raise serializers.ValidationError("Bukti pembayaran diperlukan untuk metode transfer.")
        if data['metode'] == 'cash' and data.get('bukti_transfer'):
            raise serializers.ValidationError("Bukti pembayaran tidak perlu disediakan untuk metode cash/tunai.")
        return data

    def create(self, validated_data):
        pesanan_data = validated_data.pop('pesanan')
        pesanan = PesananSerializer.create(PesananSerializer(), validated_data=pesanan_data)
        pembayaran = Pembayaran.objects.create(pesanan=pesanan, **validated_data)
        return pembayaran
