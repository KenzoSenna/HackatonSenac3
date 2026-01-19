from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, DadosClinicos, PrevioHistoricoMedico
from .forms import PacienteForm, DadosClinicosForm, PrevioHistoricoMedicoForm

def ficha_view(request):
    form = PacienteForm()
    return render(request, 'ficha.html', {'form': form})

def submit_paciente_form(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()
            return redirect('atendimento', paciente_id=paciente.id)
    else:
        form = PacienteForm()
    return render(request, 'ficha.html', {'form': form})

def submit_atendimento_form(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = DadosClinicosForm(request.POST)
        if form.is_valid():
            dados = form.save(commit=False)
            dados.paciente = paciente
            dados.save()
            return redirect('historico', paciente_id=paciente.id)
    else:
        form = DadosClinicosForm()
    return render(request, 'registro_historico.html', {'form': form, 'paciente': paciente})

def submit_historico_form(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = PrevioHistoricoMedicoForm(request.POST)
        if form.is_valid():
            historico = form.save(commit=False)
            historico.paciente = paciente
            historico.save()
            return redirect('success_page')
    else:
        form = PrevioHistoricoMedicoForm()
    return render(request, 'registro_historico.html', {'form': form, 'paciente': paciente})

def success_view(request):
    return render(request, 'success.html')

def pesquisar_paciente(request):
    cpf = request.GET.get('cpf')
    paciente = None
    dados = None
    historico = None

    if cpf:
        try:
            paciente = Paciente.objects.get(cpf=cpf)
            dados = DadosClinicos.objects.filter(paciente=paciente).last()
            historico = PrevioHistoricoMedico.objects.filter(paciente=paciente).last()
        except Paciente.DoesNotExist:
            paciente = None

    return render(request, 'pesquisa.html', {
        'paciente': paciente,
        'dados': dados,
        'historico': historico
    })
