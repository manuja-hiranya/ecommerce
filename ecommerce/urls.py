from django.contrib import admin
from django.urls import path
from store.views import home, shop, beauty, spices, fashion, contact, about  # Import the views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('categories/beauty/', beauty, name='beauty'),
    path('categories/spices/', spices, name='spices'),
    path('categories/fashion/', fashion, name='fashion'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
