from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.cache import cache_page
from rest_framework.pagination import PageNumberPagination
# app
from .models import Kategori, Menu, Pesanan, ItemPesanan, Pembayaran
from .serializers import KategoriSerializer, MenuSerializer, PesananSerializer, PembayaranSerializer

# Kategori Views
@csrf_exempt 
@api_view(['GET', 'POST'])
# @cache_page(60 * 1) 
def kategori_list(request):
    if request.method == 'GET':

        kategori = Kategori.objects.all().order_by('-id')
        serializer = KategoriSerializer(kategori, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt 
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
# @csrf_exempt 
@api_view(['GET', 'POST'])
# @cache_page(60 * 15)
def menu_list(request):
    if request.method == 'GET':
        menus = Menu.objects.all().order_by('-id')
        serializer = MenuSerializer(menus, many=True, context={'request': request})
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt 
@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Pesanan Views
@csrf_exempt 
@api_view(['GET', 'POST'])
def pesanan_list(request):
    if request.method == 'GET':
        pesanan = Pesanan.objects.all()
        serializer = PesananSerializer(pesanan, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PesananSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt 
@api_view(['GET', 'PUT', 'DELETE'])
def pesanan_detail(request, pk):
    try:
        pesanan = Pesanan.objects.get(pk=pk)
    except Pesanan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PesananSerializer(pesanan, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PesananSerializer(pesanan, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Pembayaran Views
@csrf_exempt 
@api_view(['GET', 'POST'])
def pembayaran_list(request):
    if request.method == 'GET':
        pembayaran = Pembayaran.objects.all()
        serializer = PembayaranSerializer(pembayaran, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PembayaranSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt 
@api_view(['GET', 'PUT', 'DELETE'])
def pembayaran_detail(request, pk):
    try:
        pembayaran = Pembayaran.objects.get(pk=pk)
    except Pembayaran.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PembayaranSerializer(pembayaran, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PembayaranSerializer(pembayaran, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pembayaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
