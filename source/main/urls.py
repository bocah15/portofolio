from django.conf.urls import url, include
from . import views
from dosen.models import Dosen
from kehadiran.models import Kehadiran
from kehadiran import views as kehadiran_views

urlpatterns = [ url(r'^$', views.utama, name='utama'),
				url(r'^dosen/', views.utamaDosen, name='utamaDosen'),

				url(r'^login/$', views.login_view, name='login_view'),
				url(r'^logout/$', views.logout_view, name='logout_view'),

				url(r'^profil/', include('dosen.urls')),
				url(r'^daftar_kehadiran/', kehadiran_views.daftar_kehadiran),
			    url(r'^pengajuan_kehadiran/', kehadiran_views.pengajuan_kehadiran),

			    url(r'^ganti/sibuk/', views.sibuk, name='sibuk'),

			    url(r'^hapus/deletekehadiran/', kehadiran_views.deletekehadiran, name='deletekehadiran'),
			    url(r'^edit/editkehadiran/$', kehadiran_views.editkehadiran, name='editkehadiran'),
			    url(r'^edit/editkehadiran/update/', kehadiran_views.updatekehadiran, name='updatekehadiran'),
			    
			    url(r'^kehadiran/', views.kehadiran, name='kehadiran'),
			    url(r'^kehadiranDosen/', views.kehadiranDosen, name='kehadiranDosen'),
			    
			    url(r'^hapus/reset_all/', views.reset, name='reset'),
]