from django.conf.urls import url, include
from . import views
# from kehadiran.models import Kehadiran

urlpatterns = [ url(r'^$', views.profil, name='profil'),
				url(r'^edit/$', views.edit_profil, name='edit_profil'),
				url(r'^edit/update/$', views.update_profil, name='edit_profil'),
				# url(r'^daftar_kehadiran/', include('kehadiran.urls')),
]