from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Projetos, Atividades

def index(request):
    ultimos_projetos = Projetos.objects.order_by('id')[:5]
    context = {'ultimos_projetos': ultimos_projetos}
    return render(request, 'projetos/index.html', context)

def detail(request, projetos_id):
    projeto = get_object_or_404(Projetos, pk=projetos_id)
    return render(request, 'projetos/detail.html', {'projeto': projeto})

def addatividade(request, projetos_id):
    projeto = get_object_or_404(Projetos, pk=projetos_id)
    nova_atividade = projeto.atividade_set.get(pk=request.POST['nome_atividade'])
    return render(request, 'projetos/detail.html', {'projeto':projeto})
    #return HttpResponseRedirect(reverse('projetos:results', args=(projetos.id,)))

def results(request, projetos_id):
    projeto = get_object_or_404(Projetos, pk=projetos_id)
    return render(request, 'projetos/results.html', {'projeto': projeto})