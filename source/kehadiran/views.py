from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect

from django.contrib.auth.models import User
from dosen.models import Dosen, Akun
from kehadiran.models import Kehadiran
from kehadiran.forms import KehadiranForm

# Create your views here.

# @login_required(login_url=settings.LOGIN_URL)
# def hadir(request):
#     daftar_kehadiran = None

#     if request.method == 'POST':
#         daftar_kehadiran = Kehadiran.objects.filter(dosen__id=request.session['dosen_id'])

#     return render(request, 'kehadiran/daftar_kehadiran.html', {'daftar_kehadiran':daftar_kehadiran})

@login_required(login_url=settings.LOGIN_URL)
def pengajuan_kehadiran(request):
    kode = request.session['dosen_id']
    if request.method == 'POST':
        
        jenis_kehadiran = request.POST['jenis_kehadiran']
        tanggal = request.POST['tanggal']
        waktu_Mulai = request.POST['waktu_Mulai']
        waktu_Selesai = request.POST['waktu_Selesai']
        keterangan = request.POST['keterangan']

        kehadiran = Kehadiran(
                dosen = Dosen.objects.get(id=kode),
                jenis_kehadiran = jenis_kehadiran,
                tanggal=tanggal,
                waktu_Mulai = waktu_Mulai,
                waktu_Selesai = waktu_Selesai,
                keterangan = keterangan,)
        kehadiran.save()
        # Dosen.objects.filter(id=kode).update(status=True)
        return redirect('/daftar_kehadiran/')
        # return HttpResponse(jenis_kehadiran + " waktu_Mulai : " + waktu_Mulai + " waktu_Selesai : " + waktu_Selesai + "Ket : " + keterangan + "id = " + kode)

    else:
        form = KehadiranForm()
    dosen_ini = Dosen.objects.filter(id=kode)
    user_ini = User.objects.filter(id=request.session['user_id'])
    context = {
        "form": form,
        "dosen_ini" : dosen_ini,
        "user_ini" : user_ini

    }
    return render(request, 'kehadiran/pengajuan_kehadiran.html', context)


@login_required(login_url=settings.LOGIN_URL)
def daftar_kehadiran(request):
    daftar_izin = Kehadiran.objects.filter(dosen__id=request.session['dosen_id']).order_by('tanggal','waktu_Mulai')
    user_ini = User.objects.filter(id=request.session['user_id'])
    dosen_ini = Dosen.objects.filter(id=request.session['dosen_id'])
    context = {
        'dosen_ini':dosen_ini,
        'daftar_izin':daftar_izin,
        'user_ini':user_ini
    }


    return render(request, 'kehadiran/daftar_kehadiran.html', context)

@login_required(login_url=settings.LOGIN_URL)
def deletekehadiran(request):
    hapus = request.GET['hapus']
    Kehadiran.objects.filter(id=hapus).delete()
    return redirect('/daftar_kehadiran/')


@login_required(login_url=settings.LOGIN_URL)
def editkehadiran(request):
    edit = request.GET.get('editini')
    edit_ini = Kehadiran.objects.filter(id=edit)

    daftar_izin = Kehadiran.objects.filter(dosen__id=request.session['dosen_id']).order_by('waktu_Mulai')
    user_ini = User.objects.filter(id=request.session['user_id'])
    dosen_ini = Dosen.objects.filter(id=request.session['dosen_id'])
    context = {
        'dosen_ini':dosen_ini,
        'daftar_izin':daftar_izin,
        'user_ini':user_ini,
        'edit_ini':edit_ini,
        'kode':edit
    }

    return render(request, 'kehadiran/edit_kehadiran.html', context)

@login_required(login_url=settings.LOGIN_URL)
def updatekehadiran(request):
    update = request.GET.get('updateKehadiran')

    jenis_kehadiran = request.GET['jenis_kehadiran']
    tanggal = request.GET['tanggal']
    waktu_Mulai = request.GET['waktu_Mulai']
    waktu_Selesai = request.GET['waktu_Selesai']
    keterangan = request.GET.get('keterangan')
    # return HttpResponse("jenis_kehadiran = " + keterangan)
    Kehadiran.objects.filter(id=update).update(
        jenis_kehadiran=jenis_kehadiran,tanggal=tanggal,waktu_Mulai=waktu_Mulai,
        waktu_Selesai=waktu_Selesai,keterangan=keterangan
        )
    return redirect('/daftar_kehadiran/')