from django.contrib import admin
from django.urls import path
from store.views import home  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add this route
]
