import datetime

from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Projetos, Atividades

class IndexView(generic.ListView):
    template_name = 'projetos/index.html'
    context_object_name = 'latest_projetos_list'

    def get_queryset(self):
        return Projetos.objects.order_by('id')[:5]

class ResultsView(generic.DetailView):
    model = Projetos
    template_name = 'projetos/results.html'

def detail(request, projetos_id):
    projeto = get_object_or_404(Projetos, pk=projetos_id)
    lista_atividades = projeto.atividades_set.all()
    quantidade_atividades = lista_atividades.count()
    atividades_finalizadas = projeto.atividades_set.filter(finalizada = True)
    quantidade_finalizadas = atividades_finalizadas.count()
    progresso = round(quantidade_finalizadas * 100 / quantidade_atividades, 2)
    list_atividade_maior_prazo = projeto.atividades_set.order_by('-data_fim')[:1]
    atividade_maior_prazo = list_atividade_maior_prazo.first()
    previsao_atrazo = atividade_maior_prazo.data_fim > projeto.data_fim
    atrasado = quantidade_atividades > quantidade_finalizadas and atividade_maior_prazo.data_fim < timezone.now()
    context = {
        'lista_atividades': lista_atividades,
        'quantidade_finalizadas': quantidade_finalizadas,
        'progresso': progresso,
        'projeto': projeto,
        'previsao_atrazo': previsao_atrazo,
        'atrasado': atrasado,
        'quantidade_atividades': quantidade_atividades,
        'atividade_maior_prazo_data_fim': atividade_maior_prazo.data_fim,
        'agora': timezone.now(),
        'quantidade_atividades_andamento': quantidade_atividades - quantidade_finalizadas,
    }
    return render(request, 'projetos/detail.html', context)

def atividade(request, projetos_id):
    projeto = get_object_or_404(Projetos, pk=projetos_id)
    try:
        adividade_selecionada = projeto.atividades_set.get(pk=request.POST['atividade'])
    except (KeyError, Atividades.DoesNotExist):
        return render(request, 'projetos/detail.html', {
            'projeto': projeto,
            'error_message': "Vc não selecionou uma atividade.",
        })
    else:
        adividade_selecionada.nome_atividade = ''
        adividade_selecionada.save()
        return HttpResponseRedirect(reverse('projetos:results', args=(projeto.id,)))
