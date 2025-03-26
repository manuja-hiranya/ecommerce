from django.shortcuts import render

def home(request):
    return render(request, 'store/index.html')

def shop(request):
    return render(request, 'store/shop.html')

def beauty(request):
    return render(request, 'store/beauty.html')

def spices(request):
    return render(request, 'store/spices.html')

def fashion(request):
    return render(request, 'store/fashion.html')

def contact(request):
    return render(request, 'store/contact.html')

def about(request):
    return render(request, 'store/about.html')
