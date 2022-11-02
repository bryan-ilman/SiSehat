from django.urls import path
from . import views
import obat

urlpatterns = [
    path('lihat-obat/', views.lihat_obat, name='lihat_obat'),
    path('lihat-obat/<str:pasien>', views.get_obat, name='get_obat'),
    path('add-obat/<str:pasien>', views.add_obat, name='add_obat'),
]