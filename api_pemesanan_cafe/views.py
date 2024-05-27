from django.shortcuts import render
# <<<<<<< HEAD

# =======
# >>>>>>> d60a92416265a14620e141604e60948efe75a48c

def index(request):
    
    return render(request, 'index.html')

def detail(request):
    
    return render(request, 'detail.html')
