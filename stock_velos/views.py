from django.shortcuts import render, redirect
from .models import Velo
from .forms import Velosform
from django.contrib.auth.decorators import login_required

@login_required(login_url='/compte/login')
def stock_velos(request):
    velos_objets = Velo.objects.all()

    context = {
        'velosObjets': velos_objets
    }

    return render(request, 'stock_velos/stock_velos.html', context)

@login_required(login_url='/compte/login')
def nouveau_velo(request):
    formVelo = Velosform()
    if request.method == 'POST':
        formVelo = Velosform(request.POST)
        if formVelo.is_valid():
            formVelo.save()
            return redirect('/stock_velos')

    context = {
        'formVelo': formVelo
    }
    return render(request, 'stock_velos/ajouter_velos.html', context)

@login_required(login_url='/compte/login')
def modifier_velo(request, pk):
    velo = Velo.objects.get(vel_id=pk)
    formVelo = Velosform(instance=velo)
    if request.method == 'POST':
        formVelo = Velosform(request.POST, instance=velo)
        if formVelo.is_valid():
            formVelo.save()
            return redirect('/stock_velos')

    context = {
        'formVelo': formVelo
    }
    return render(request, 'stock_velos/ajouter_velos.html', context)

@login_required(login_url='/compte/login')
def supprimer_velo(request, pk):
    velo = Velo.objects.get(vel_id=pk)
    if request.method == 'POST':
        velo.delete()
        return redirect('/stock_velos')

    context = {
        'item': velo
    }
    return render(request, 'stock_velos/supprimer_velo.html', context)


@login_required(login_url='/compte/login')
def details_velo(request, id):
    velo = Velo.objects.get(vel_id=id)
    messageDescriptionVelo = f"Il n'y a pas de remarque"
    if velo.vel_remarque is not "" :
        messageDescriptionVelo = velo.vel_remarque

    context = {
        'velo' : velo,
        'messageDescriptionVelo' : messageDescriptionVelo,
    }


    return render(request, 'stock_velos/detailsVeloClient.html', context)