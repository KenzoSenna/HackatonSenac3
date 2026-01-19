from django.shortcuts import render, redirect
from .models import Paciente, DadosClinicos, PrevioHistoricoMedico

def ficha_view(request):
    return render(request, 'ficha.html')

def atendimento_view(request):
    return render(request, 'atendimento.html')

def submit_paciente_form(request):
    if request.method == 'POST':
        paciente = Paciente.objects.create(
            nome=request.POST.get('nome'),
            data_de_nascimento=request.POST.get('dataNasc'),
            genero=request.POST.get('genero')[0].upper(),  # M/F/O
            telefone=request.POST.get('telefone'),
            email=request.POST.get('email'),
            cep=request.POST.get('cep'),
            numero_endereco=request.POST.get('numero'),
            estado_civil=request.POST.get('estadoCivil')[0].upper(),
            profissao=request.POST.get('profissao'),
            formacao_educacional=request.POST.get('formacao')
        )
        return redirect('atendimento', paciente_id=paciente.id)

    return render(request, 'ficha.html')


def submit_atendimento_form(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if request.method == 'POST':
        DadosClinicos.objects.create(
            paciente=paciente,
            razao=request.POST.get('razao'),
            tipo_sanguineo=request.POST.get('tipo_sanguineo'),
            pressao_arterial=request.POST.get('PA'),
            temperatura=request.POST.get('temperatura'),
            frequencia_respiratoria=request.POST.get('FR'),
            saturacao_oxigenio=request.POST.get('SO'),
            glicemia=request.POST.get('glicemia'),
            altura=request.POST.get('altura'),
            peso=request.POST.get('peso'),
            alergias=request.POST.get('alergias'),
            medicamentos=request.POST.get('medicamentos'),
            condicao_medica=request.POST.get('CM')
        )
        return render(request, 'atendimento.html', {'paciente': paciente})
    
def submit_historico_form(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if request.method == 'POST':
        PrevioHistoricoMedico.objects.create(
            paciente=paciente,
            internacao_anterior=request.POST.get('internacao_anterior'),
            cirurgia_anterior=request.POST.get('cirurgia_anterior'),
            doencas_familiares=request.POST.get('doencas_familiares')
        )
        return render(request, 'atendimento.html', {'paciente': paciente})


