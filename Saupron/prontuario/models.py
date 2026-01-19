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
    profissao = models.CharField(max_length='150')
    formacao_educacional = models.CharField(max_length='150')
