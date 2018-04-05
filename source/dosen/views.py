# from django.http import HttpResponse
# from django.shortcuts import render

# # Create your views here.

def home_dosen (request):
	return render(request, 'dosen/logindosen.html')
	# return HttpResponse("<h1>Login</h1>")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from dosen.models import Dosen, Akun
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	# return HttpResponse("hallo")
    profil = Dosen.objects.filter(id=request.session['dosen_id'])
    user_ini = User.objects.filter(id=request.session['user_id'])
    context = {
    	"dosen_ini": profil,
    	"user_ini": user_ini
    }
    return render(request, 'dosen/profil.html', context)

@login_required(login_url=settings.LOGIN_URL)
def edit_profil(request):
	if request.method == 'POST':
		profil = Dosen.objects.filter(id=request.session['dosen_id'])
		user_ini = User.objects.filter(id=request.session['user_id'])
		context = {
			"dosen_ini": profil,
			"user_ini": user_ini
		}
		return render(request, 'dosen/edit_profil.html', context)

@login_required(login_url=settings.LOGIN_URL)
def update_profil(request):
	kodeDosen = request.session['dosen_id']
	kodeAkun = request.session['user_id']

	userBaru = request.GET['usernameBaru']
	namaBaru = request.GET['namaBaru']
	nipBaru = request.GET['nipBaru']

	User.objects.filter(id=kodeAkun).update(username=userBaru)
	Dosen.objects.filter(id=kodeDosen).update(nama=namaBaru, nip=nipBaru)

	return redirect('/profil/')