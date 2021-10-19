from django.shortcuts import render, redirect
from .models import Local, Velo
from .forms import Localform
from django.contrib.auth.decorators import login_required


@login_required(login_url='/compte/login')
def stock_locaux(request):
    local_objets = Local.objects.all()

    context = {
        'localObjets': local_objets
    }

    return render(request, 'stock_locaux/stock_locaux.html', context)


def nouveau_local(request):
    formLocal = Localform()
    if request.method == 'POST':
        formLocal = Localform(request.POST)
        if formLocal.is_valid():
            if Local.objects.all().count() == 0:
                nb = 1
            else:
                nb = Local.objects.latest('local_id').local_num + 1
            local = Local(local_nom=formLocal.cleaned_data.get('local_nom'),
                          local_adresseposte=formLocal.cleaned_data.get('local_adresseposte'),
                          local_npa=formLocal.cleaned_data.get('local_npa'),
                          local_capacite=formLocal.cleaned_data.get('local_capacite'),
                          local_nb_velo=formLocal.cleaned_data.get('local_nb_velo'),
                          local_num=nb
                          )
            local.save()
            return redirect('/stock_locaux')

    context = {
        'formLocal': formLocal
    }
    return render(request, 'stock_locaux/ajouter_local.html', context)

def supprimer_velo(request, pk):
    velo = Velo.objects.get(vel_id=pk)
    if request.method == 'POST':
        local = Local.objects.get(local_id=velo.local_id_id)
        local.local_nb_velo -= 1
        local.save()
        velo.delete()



        return redirect('/stock_velos')

    context = {
        'item': velo
    }
    return render(request, 'stock_velos/supprimer_velo.html', context)


def nb_velos(request, num):
    velos = Velo.objects.all(local_num=num)
    velos_number = velos.count()
    Nb_velos = f'{velos_number} locations :'

    context = {
        'Nb_velos': Nb_velos,
    }

    return render(request, 'stock_locaux/stock_locaux.html', context)
