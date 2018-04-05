from django.contrib import admin
from dosen.models import Dosen, Akun

# Register your models here.

class DosenAdmin (admin.ModelAdmin):
    list_display = ['nama', 'nip','foto', 'status']
    # list_filter = ('jenis_kelamin')
    search_fields = ['nama']
    list_per_page = 25

    def get_ordering(self, request):
    	return ['nama']

admin.site.register(Dosen, DosenAdmin)

class AkunAdmin (admin.ModelAdmin):
    list_display = ['akun', 'profil', 'jenis_akun']
    list_filter = ('jenis_akun',)
    search_fields = []
    list_per_page = 25

    def get_ordering(self, request):
    	return ['jenis_akun', 'akun']

admin.site.register(Akun, AkunAdmin)
