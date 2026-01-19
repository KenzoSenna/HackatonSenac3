from django import forms
from .models import Paciente, DadosClinicos, PrevioHistoricoMedico

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome', 'data_de_nascimento', 'genero', 'telefone','cpf', 'email',
            'cep', 'numero_endereco', 'estado_civil', 'profissao', 'formacao_educacional'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'id': 'nome', 'class': 'input'}),
            'data_de_nascimento': forms.DateInput(attrs={'id': 'dataNasc', 'class': 'input', 'type': 'date'}),
            'genero': forms.Select(attrs={'id': 'genero', 'class': 'input'}),
            'telefone': forms.TextInput(attrs={'id': 'telefone', 'class': 'input'}),
            'cpf': forms.TextInput(attrs={'id': 'cpf', 'class': 'input'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'class': 'input'}),
            'cep': forms.TextInput(attrs={'id': 'cep', 'class': 'input'}),
            'numero_endereco': forms.NumberInput(attrs={'id': 'numero', 'class': 'inputMenor'}),
            'estado_civil': forms.Select(attrs={'id': 'estadoCivil', 'class': 'input'}),
            'profissao': forms.TextInput(attrs={'id': 'profissao', 'class': 'input'}),
            'formacao_educacional': forms.TextInput(attrs={'id': 'formacao', 'class': 'input'}),
        }


class DadosClinicosForm(forms.ModelForm):
    class Meta:
        model = DadosClinicos
        fields = [
            'razao', 'tipo_sanguineo', 'pressao_arterial', 'temperatura',
            'frequencia_respiratoria', 'saturacao_oxigenio', 'glicemia',
            'altura', 'peso', 'alergias', 'medicamentos', 'condicao_medica'
        ]
        widgets = {
            'razao': forms.TextInput(attrs={'id': 'razao', 'class': 'input'}),
            'tipo_sanguineo': forms.Select(attrs={'id': 'tipo_sanguineo', 'class': 'input'}),
            'pressao_arterial': forms.TextInput(attrs={'id': 'PA', 'class': 'input'}),
            'temperatura': forms.TextInput(attrs={'id': 'temperatura', 'class': 'input'}),
            'frequencia_respiratoria': forms.NumberInput(attrs={'id': 'FR', 'class': 'input'}),
            'saturacao_oxigenio': forms.TextInput(attrs={'id': 'SO', 'class': 'input'}),
            'glicemia': forms.NumberInput(attrs={'id': 'glicemia', 'class': 'input'}),
            'altura': forms.NumberInput(attrs={'id': 'altura', 'class': 'input'}),
            'peso': forms.NumberInput(attrs={'id': 'peso', 'class': 'input'}),
            'alergias': forms.TextInput(attrs={'id': 'alergias', 'class': 'input'}),
            'medicamentos': forms.TextInput(attrs={'id': 'medicamentos', 'class': 'input'}),
            'condicao_medica': forms.TextInput(attrs={'id': 'CM', 'class': 'input'}),
        }


class PrevioHistoricoMedicoForm(forms.ModelForm):
    class Meta:
        model = PrevioHistoricoMedico
        fields = ['internacao_anterior', 'cirurgia_anterior', 'doencas_familiares']
        widgets = {
            'internacao_anterior': forms.TextInput(attrs={'id': 'internacao_anterior', 'class': 'input'}),
            'cirurgia_anterior': forms.TextInput(attrs={'id': 'cirurgia_anterior', 'class': 'input'}),
            'doencas_familiares': forms.TextInput(attrs={'id': 'doencas_familiares', 'class': 'input'}),
        }