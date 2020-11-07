from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Projetos, Atividades

class IndexView(generic.ListView):
    template_name = 'projetos/index.html'
    context_object_name = 'ultimos_projetos'

    def get_queryset(self):
        return Projetos.objects.order_by('id')[:5]

class DetailView(generic.DetailView):
    model = Projetos
    template_name = 'projetos/detail.html'

class ResultsView(generic.DetailView):
    model = Projetos
    template_name = 'projetos/results.html'

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
        adividade_selecionada.nome_atividade = 'A escolha da tecnologia'
        adividade_selecionada.save()
        return HttpResponseRedirect(reverse('projetos:results', args=(projeto.id,)))
