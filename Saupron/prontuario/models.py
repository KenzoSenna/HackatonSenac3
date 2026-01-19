from django.db import models

# Create your models here.

class Paciente(models.Model):
    ESTADO_CIVIL_CHOICES = [('S', 'Solteira(o)'), ('C', 'Casada(o)'), ('D', 'Divorciada(o)'), ('V', 'Viuva(o)'), ('O', 'Outro')]
    GENERO_CHOICES = [ ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'), ]
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_de_nascimento = models.DateField(auto_now=False,
    auto_now_add=False, null=False)
    genero = models.CharField(max_length=1,
        choices=GENERO_CHOICES,
        default='M'
    )
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    cep = models.CharField(max_length=10)
    numero_endereco = models.IntegerField()
    estado_civil = models.CharField(
        max_length=1,
        choices=ESTADO_CIVIL_CHOICES,
        default='S'
    )
    profissao = models.CharField(max_length=150)
    formacao_educacional = models.CharField(max_length=150)


class DadosClinicos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    razao = models.CharField(max_length=255, null=False)
    TIPO_SANGUINEO_CHOICES = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')]
    tipo_sanguineo = models.CharField(max_length=3, choices=TIPO_SANGUINEO_CHOICES, default='O+')
    pressao_arterial = models.IntegerField()
    temperatura = models.CharField(max_length=4)
    frequencia_respiratoria = models.IntegerField()
    saturacao_oxigenio = models.CharField(max_length=4)
    glicemia = models.IntegerField()
    altura = models.IntegerField()
    peso = models.IntegerField()
    alergias = models.CharField(max_length=255)
    medicamentos = models.CharField(max_length=255)
    condicao_medica = models.CharField(max_length=255)

class PrevioHistoricoMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    internacao_anterior = models.CharField(max_length=255)
    cirurgia_anterior = models.CharField(max_length=255)
    doencas_familiares = models.CharField(max_length=255)

# class RevisaoSistemas(models.Model):
#     # sensorial = models.
#     pass