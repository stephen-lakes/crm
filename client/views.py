from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Client

from .forms import AddClientForm

@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)

    return render(request, 'client/clients_list.html', {
        'clients': clients
    })


@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    return render(request, 'client/clients_detail.html', {
        'client': client
    })


@login_required
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()

            messages.success(request, 'Client was created')

            return redirect('clients_list')
    else:
        form = AddClientForm()

    return render(request, 'client/add_client.html', {
        'form': form
    })


@login_required
def clients_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()

    messages.success(request, 'The client was deleted')

    return redirect('clients_list')


@login_required
def clients_edit(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()

            messages.success(request, 'Changes was saved')

            return redirect('clients_list')
    else:
        form = AddClientForm(instance=client)

    return render(request, 'client/clients_edit.html', {
        'form': form
    })
