from django.forms import ModelForm
from django import forms
from kehadiran.models import Kehadiran

class KehadiranForm(ModelForm):
    JENIS_KEHADIRAN_CHOICES = (
        ('sibuk', 'Sibuk'),
        ('senggang', 'Senggang'),
        ('pulang', 'Pulang'),
        ('ttd', 'Khusus ttd'),
    )
    
    jenis_kehadiran = forms.ChoiceField(
        choices=JENIS_KEHADIRAN_CHOICES,widget=forms.Select(
            attrs={'name':'jenis_kehadiran'}
            )
        )
    tanggal = forms.DateField(
        widget=forms.DateInput(attrs={
            'class':'form-control','id':'date', 'name':'tanggal', 'placeholder':'YYYY-MM-DD', 'type':'text'}
            )
        )

    waktu_Mulai = forms.DateField(
        widget=forms.DateInput(attrs={
            'name':'waktu_Mulai','class':'form-control input-small','id':'waktuAwal','type':'text'}
            )
        )
    waktu_Selesai = forms.DateField(
        widget=forms.DateInput(attrs={
            'name':'waktu_Selesai','class':'form-control input-small','id':'waktuAkhir','type':'text'}
            )
        )
    keterangan = forms.CharField(widget=forms.Textarea(attrs={'name':'keterangan','class':'form-control input-small col-md-5 mb-3','cols':30, 'rows': 5}))

    class Meta:
        model = Kehadiran

        fields = ['jenis_kehadiran','tanggal','waktu_Mulai','waktu_Selesai', 'keterangan']

        # fields = ['jenis_kehadiran', 'waktu_Mulai', 'waktu_Selesai', 'keterangan']
        # labels = {
        #     'jenis_kehadiran':"Status",
        #     'waktu_Mulai':'Waktu Mulai',
        #     'waktu_Selesai':'Waktu Berhenti',
        #     'keterangan':'Keterangan',
        # }
        # error_messages = {
        #     'jenis_kehadiran': {
        #         'required': 'Anda harus memilih jenis izin'
        #     },
        #     'waktu_mulai' : {
        #         'required': "Anda harus menentukan tanggal izin dimulai"
        #     },
        #     'waktu_berhenti' : {
        #         'required': "Anda harus menentukan tanggal izin berakhir"
        #     },
        #     'alasan':{
        #         'required': "Alasan harus diisi agar dapat disetujui oleh HRD"
        #     }
        # }
        # widgets = {
        #     'alasan': forms.Textarea(attrs={ 'cols':50, 'rows': 10 })
        # }