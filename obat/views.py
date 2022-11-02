import datetime
import re

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

from obat.forms import ObatForm
from obat.models import Obat
from registrasi.models import Dokter, Pasien

@login_required(login_url='/registrasi/halaman-masuk/')
def lihat_obat(request):
    if request.COOKIES.get('user_type') == 'pasien':
        pasien = Pasien.objects.get(user=request.user)
        data_obat = Obat.objects.filter(pasien=pasien)
    elif request.COOKIES.get('user_type') == 'dokter':
        dokter = Dokter.objects.get(user=request.user)
        data_obat = Obat.objects.filter(dokter=dokter)
    else:
        return redirect('registrasi:halaman_registrasi')

    data_pasien = Pasien.objects.all()

    context = {
        'list_obat': data_obat,
        'dokter': (request.COOKIES.get('user_type') == 'dokter'),
        'list_pasien': data_pasien,
        'form': ObatForm(request.POST)
    }
    return render(request, 'lihat_obat.html', context)

@login_required(login_url='/registrasi/halaman-masuk/')
def get_obat(request, pasien=None):
    if request.COOKIES.get('user_type') == 'pasien':
        pasien = Pasien.objects.get(user=request.user)
        data_obat = serializers.serialize("json", Obat.objects.filter(pasien=pasien))
    elif request.COOKIES.get('user_type') == 'dokter':
        pasien = Pasien.objects.get(nomor_induk_kependudukan=pasien)
        dokter = Dokter.objects.get(user=request.user)
        data_obat = serializers.serialize("json", Obat.objects.filter(pasien=pasien, dokter=dokter))
    else:
        return redirect('registrasi:halaman_registrasi')

    return HttpResponse(data_obat, content_type="application/json")

@login_required(login_url='/registrasi/halaman-masuk/')
def add_obat(request, pasien):
    if request.COOKIES.get('user_type') == 'dokter':
        form = ObatForm(request.POST)

        if request.method == 'POST':
            if form.is_valid():
                obat = form.save(commit=False)
                obat.pasien = Pasien.objects.get(nomor_induk_kependudukan=pasien)
                obat.dokter = Dokter.objects.get(user=request.user)
                obat.tanggal = str(datetime.datetime.now().strftime('%b %d %Y %H:%M:%S'))
                obat.save()
                return lihat_obat(request)

            return HttpResponseNotFound()        
        return HttpResponseNotFound()
    else:
        return redirect('registrasi:halaman_registrasi')

