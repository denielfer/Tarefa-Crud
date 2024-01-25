from django.shortcuts import render,HttpResponse
from .models import Tarefa
from .forms import Tarefa_form

# Create your views here.
def home(request):
    return HttpResponse('oi')

def tarefas(request):
    form = Tarefa_form()
    if request.method == 'POST':
        if "save" in request.POST:
            id = request.POST.get('save')
            print(id)
            if not id:
                form = Tarefa_form(request.POST)
            else:
                print(request.POST)
                tarefa_edit = Tarefa.objects.get( id = id )
                form = Tarefa_form(request.POST,instance = tarefa_edit)
            form.save()
            form = Tarefa_form()
        elif 'deletar' in request.POST:
            Tarefa.objects.get( id = request.POST.get('deletar') ).delete()
        elif 'edit' in request.POST:
            tarefa_edit = Tarefa.objects.get( id = request.POST.get('edit') )
            form = Tarefa_form(instance = tarefa_edit)
    context = {
        "tarefas": Tarefa.objects.all(),
        "form": form
    }
    return render(request,'view_tarefas.html',context=context)