from django import forms

from apps.gallery.models import Fotografia

class FotografiaForms(forms.ModelForm):
	class Meta:
		model = Fotografia
		exclude = ['publicada',]
		labels = {
			'name': 'Nome',
			'subtitle': 'Legenda',
			'category': 'Categoria',
			'description': 'Descrição',
			'data_fotografia': 'Data de Registro',
			'usuario': 'Usuário'
        }
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                'type': 'date',
                'class':'form-control'
			}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
		}