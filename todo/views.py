from django import http
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from todo.models import Todo
from todo.forms import TodoForm

@login_required(login_url='/admin/login/')
def add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect(reverse('todo.list'))
    
    return render_to_response('add.html', {'form':form},
                              context_instance=RequestContext(request))

@login_required(login_url='/admin/login/')
def list(request):
    return render_to_response('list.html', {'objects':Todo.objects.all()})

@login_required(login_url='/admin/login/')
def edit(request, pk):
    instance = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect(reverse('todo.list'))
    
    return render_to_response('edit.html', {'form':form},
                              context_instance=RequestContext(request))


