from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Kategori, Menu, Pesanan, ItemPesanan, Pembayaran
from .serializers import KategoriSerializer, MenuSerializer, PesananSerializer, PembayaranSerializer

# Kategori Views
@api_view(['GET', 'POST'])
def kategori_list(request):
    if request.method == 'GET':
        kategori = Kategori.objects.all()
        serializer = KategoriSerializer(kategori, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def kategori_detail(request, pk):
    try:
        kategori = Kategori.objects.get(pk=pk)
    except Kategori.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KategoriSerializer(kategori)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        kategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Menu Views

@api_view(['GET', 'POST'])
def menu_list(request):
    if request.method == 'GET':
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Pesanan Views

@api_view(['GET', 'POST'])
def pesanan_list(request):
    if request.method == 'GET':
        pesanan = Pesanan.objects.all()
        serializer = PesananSerializer(pesanan, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PesananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pesanan_detail(request, pk):
    try:
        pesanan = Pesanan.objects.get(pk=pk)
    except Pesanan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PesananSerializer(pesanan)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PesananSerializer(pesanan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Pembayaran Views

@api_view(['GET', 'POST'])
def pembayaran_list(request):
    if request.method == 'GET':
        pembayaran = Pembayaran.objects.all()
        serializer = PembayaranSerializer(pembayaran, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PembayaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pembayaran_detail(request, pk):
    try:
        pembayaran = Pembayaran.objects.get(pk=pk)
    except Pembayaran.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PembayaranSerializer(pembayaran)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PembayaranSerializer(pembayaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pembayaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
