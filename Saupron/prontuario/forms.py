from django import forms
from .models import (Paciente, DadosClinicos, PrevioHistoricoMedico)

# class PacienteForm(forms.Form):
#     class Meta:
#         model = Paciente
#         fields = ['nome', 'genero', 'telefone', 'email', 'cep',
#      'numero_endereco', 'estado_civil', 'profissao', 'formacao_educacional']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'genero': forms.ChoiceField()
#         }