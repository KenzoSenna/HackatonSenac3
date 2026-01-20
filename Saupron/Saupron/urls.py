from django.contrib import admin
from django.urls import path
from prontuario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),

    # path('', ficha_view, name='ficha'),
    path('ficha/', submit_paciente_form, name='submit_paciente_form'),
     
    path('atendimento/', submit_atendimento_form, name='atendimento'),

    path('success/', success_view, name='success_page'),
    
    path('pesquisa/', pesquisar_paciente, name='pesquisar_paciente'),
]



