from django.contrib import admin
from kehadiran.models import Kehadiran

# Register your models here.
class KehadiranAdmin (admin.ModelAdmin):
    list_display = ['dosen', 'jenis_kehadiran', 'tanggal', 'waktu_Mulai', 'waktu_Selesai', 'keterangan','status']
    list_filter = ('jenis_kehadiran','status')
    search_fields = []
    list_per_page = 25

    def get_ordering(self, request):
    	return ['dosen','tanggal','waktu_Mulai']
    	
admin.site.register(Kehadiran, KehadiranAdmin)