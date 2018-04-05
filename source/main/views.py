from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.utils import timezone

from dosen.models import Akun, Dosen
from kehadiran.models import Kehadiran
import datetime

#Search
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

#Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def kehadiran(request):
    simpan = request.GET['id']
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    hadir = Kehadiran.objects.filter(dosen__nama=simpan,tanggal=now).order_by('tanggal','waktu_Mulai')
    querykehadiran = Kehadiran.objects.filter(dosen__nama=simpan)
    context = {
        'hadir':hadir,
        'querykehadiran':querykehadiran
    }
    return render(request, 'main/kehadirandosen.html', context)

def kehadiranDosen(request):
    simpan = request.GET['id']
    hadir = Kehadiran.objects.filter(dosen__nama=simpan).order_by('tanggal','waktu_Mulai')
    querykehadiran = Kehadiran.objects.filter(dosen__nama=simpan)
    context = {
        'hadir':hadir,
        'querykehadiran':querykehadiran
    }
    return render(request, 'main/kehadirandosen2.html', context)


def reset(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    Kehadiran.objects.filter(tanggal=now).delete()
    Dosen.objects.update(status=True)
    return redirect('/dosen/')
    # return HttpResponse(now)

def utama(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    querydosen = Dosen.objects.all()
    querykehadiran = Kehadiran.objects.filter(tanggal=now)

    jam = datetime.datetime.now().strftime("%H")
    menit = datetime.datetime.now().strftime("%M")
    detik = datetime.datetime.now().strftime("%S")
    
    paginator = Paginator(querydosen, 9)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        querset = paginator.page(paginator.num_pages)


    query = request.GET.get("q")
    if query:
        querydosen = Dosen.objects.filter(nama__icontains=query)
        paginator = Paginator(querydosen, 9)

        page = request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            querset = paginator.page(paginator.num_pages)

        # queryset = Dosen.objects.filter(nama__icontains=query)
    context = {
        "object_kehadiran": querykehadiran,
        "now":now,
        "jam":jam,
        "detik":detik,
        "menit":menit,
        "object_dosen": queryset,
        "jenis_kehadiran" : "Jenis Kehadiran",
    }

    return render(request, "main/home.html", context)

    def __str__(self):
        return self.Kehadiran.dosen

def utamaDosen(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    querydosen = Dosen.objects.all()
    querykehadiran = Kehadiran.objects.filter(tanggal=now)

    jam = datetime.datetime.now().strftime("%H")
    menit = datetime.datetime.now().strftime("%M")
    detik = datetime.datetime.now().strftime("%S")
    
    paginator = Paginator(querydosen, 9)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        querset = paginator.page(paginator.num_pages)


    query = request.GET.get("q")
    if query:
        querydosen = Dosen.objects.filter(nama__icontains=query)
        paginator = Paginator(querydosen, 9)

        page = request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            querset = paginator.page(paginator.num_pages)

        # queryset = Dosen.objects.filter(nama__icontains=query)
    context = {
        "object_kehadiran": querykehadiran,
        "now":now,
        "jam":jam,
        "menit":menit,
        "detik":detik,
        "object_dosen": queryset,
        "jenis_kehadiran" : "Jenis Kehadiran",
    }

    return render(request, "main/homeDosen.html", context)

    def __str__(self):
        return self.Kehadiran.dosen


def sibuk(request):
    id_dosen = request.session['dosen_id']

    now = datetime.datetime.now().strftime("%Y-%m-%d")
    jam = datetime.datetime.now().strftime("%H:%M %p")
    # menit = datetime.datetime.now().strftime("%M")
    # if (h == jam && m >= menit) || (h > jam && (m >= menit || m <= menit):

    cek = Dosen.objects.filter(id=id_dosen, status=False)
    if cek:
        Dosen.objects.filter(id=id_dosen).update(status=True)
        Kehadiran.objects.filter(dosen_id=id_dosen,tanggal=now, waktu_Mulai__lte=jam,waktu_Selesai__gte=jam).update(status=True)
    else:
        Dosen.objects.filter(id=id_dosen).update(status=False)
        Kehadiran.objects.filter(dosen_id=id_dosen,tanggal=now, waktu_Mulai__lte=jam,waktu_Selesai__gte=jam).update(status=False)
        # for cari in hadir:
        #     jam1 = hadir.waktu_Mulai, "%H"
        #     menit1 = hadir.waktu_Mulai, "%i"
        #     if (jam == jam1 and menit >= menit1) or (jam > jam1 and (menit >= menit1 or menit <= menit1)):
        #         cari.update(status=False)
    return redirect('/profil/')


def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # hai = request.POST['username']
        # return HttpResponse("Hallo " + hai.id)
        if user is not None:
            if user.is_active:
                try:
                    akun = Akun.objects.get(akun=user.id)
                    login(request, user)

                    request.session['user_id'] = user.id
                    request.session['dosen_id'] = akun.profil.id
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']

                    # Dosen.objects.filter(id=akun.profil.id).update(status=True)
                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data dosen, silahkan hubungi administrator')
                return redirect('/profil')
            else:   
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')