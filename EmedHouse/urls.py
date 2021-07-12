
from medicalapp import urls
from chatbot import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('customer/',include('customer.urls')),
    path('',include('medicalapp.urls')),
    path('admin/', admin.site.urls),
    path('chatbot/',include('chatbot.urls')),
    path('lab/',include('lab.urls')),
]
