from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, DadosClinicos
from .forms import PacienteForm, DadosClinicosForm
from django.contrib import messages
from .forms import PacienteSearchForm


def ficha_view(request):
    form = PacienteForm()
    return render(request, 'ficha.html', {'form': form})

def submit_paciente_form(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()
            return render(request, 'successo_aaee.html')
    else:
        form = PacienteForm()
    return render(request, 'ficha.html', {'form': form})

def submit_atendimento_form(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        try:
            paciente = Paciente.objects.get(cpf=cpf)
        except Paciente.DoesNotExist:
            messages.error(request, "Paciente com este CPF não foi encontrado.")
            form = DadosClinicosForm(request.POST)
            return render(request, 'atendimento.html', {'form': form})

        form = DadosClinicosForm(request.POST)
        if form.is_valid():
            dados = form.save(commit=False)
            dados.paciente = paciente
            dados.save()
            return render(request, 'successo_aaee.html')
    else:
        form = DadosClinicosForm()

    return render(request, 'atendimento.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')

def pesquisar_paciente(request):
    cpf = request.GET.get('cpf')  # pega o CPF da querystring
    paciente = None
    dados = None
    

    if cpf:  # só tenta buscar se o usuário digitou algo
        try:
            paciente = Paciente.objects.get(cpf=cpf)
            dados = DadosClinicos.objects.filter(paciente=paciente).last()
        except Paciente.DoesNotExist:
            messages.error(request, "Nenhum paciente encontrado com este CPF.")
            

    return render(request, 'pesquisar_paciente.html', {
        'paciente': paciente,
        'dados': dados
    })


def home_view(request):
    return render(request, 'home.html')

