from django.db import models

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_kategori

class Menu(models.Model):
    nama = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='menu_images/')
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Kategori, related_name='menus', on_delete=models.CASCADE)
    tersedia = models.BooleanField(default=True)

    def __str__(self):
        return self.nama

class Pesanan(models.Model): 
    nomor_meja = models.IntegerField()
    keterangan = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def total_harga(self):
        total = sum(item.total_harga() for item in self.items.all())
        return total
    
    def __str__(self):
        return str(f'Nomor Meja {self.nomor_meja}')

class ItemPesanan(models.Model):
    pesanan = models.ForeignKey(Pesanan, related_name='items', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    jumlah_menu = models.IntegerField()

    def total_harga(self):
        return self.menu.harga * self.jumlah_menu
    
    def __str__(self):
        return str(f'Pesanan Meja {self.pesanan.nomor_meja}')

class Pembayaran(models.Model):
    PEMBAYARAN_METODE = [
        ('transfer', 'Transfer'),
        ('cash', 'Cash'),
    ]
    STATUS_CHOICES = [
        ('proses', 'Proses'),
        ('selesai', 'Selesai'),
    ]
    pesanan = models.OneToOneField(Pesanan, related_name='pembayaran', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='proses')
    nama_pemesan = models.CharField(max_length=100)
    nomor_hp = models.CharField(max_length=16, default='+62')
    metode = models.CharField(choices=PEMBAYARAN_METODE, max_length=50)
    bukti_transfer = models.ImageField(upload_to='payment_proofs/', null=True, blank=True)

    def __str__(self):
        return f'{self.nama_pemesan} - {self.metode}'

    def konversi_nomor_hp(self):
        if self.nomor_hp.startswith('0'):
            self.nomor_hp = '+62' + self.nomor_hp[1:]
        return self.nomor_hp
