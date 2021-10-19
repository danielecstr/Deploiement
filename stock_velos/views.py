from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Velo, Local
from .forms import Velosform, Velosform_modifier
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
@login_required(login_url='/compte/login')
def stock_velos(request):
    velos_objets = Velo.objects.all()

    context = {
        'velosObjets': velos_objets
    }

    return render(request, 'stock_velos/stock_velos.html', context)

@staff_member_required
@login_required(login_url='/compte/login')
def nouveau_velo(request):
    formVelo = Velosform()
    if request.method == 'POST':
        formVelo = Velosform(request.POST)
        if formVelo.is_valid():
            if Velo.objects.all().count() == 0:
                nb = 1
            else:
                nb = Velo.objects.latest('vel_id').vel_num + 1
            velo = Velo(vel_num_cadre=formVelo.cleaned_data.get('vel_num_cadre'),
                        vel_nom=formVelo.cleaned_data.get('vel_nom'),
                        vel_marque=formVelo.cleaned_data.get('vel_marque'),
                        vel_couleur=formVelo.cleaned_data.get('vel_couleur'),
                        vel_type=formVelo.cleaned_data.get('vel_type'),
                        vel_photo=formVelo.cleaned_data.get('vel_photo'),
                        vel_statut=formVelo.cleaned_data.get('vel_statut'),
                        vel_etat=formVelo.cleaned_data.get('vel_etat'),
                        vel_remarque=formVelo.cleaned_data.get('vel_remarque'),
                        local_id=formVelo.cleaned_data.get('local_id'),
                        don_id=formVelo.cleaned_data.get('don_id'),
                        vel_num=nb)
            velo.save()
            local = Local.objects.get(local_id=formVelo.cleaned_data.get('local_id').local_id)
            local.local_nb_velo += 1
            local.save()
            return redirect('/stock_velos')

    context = {
        'formVelo': formVelo
    }
    return render(request, 'stock_velos/ajouter_velos.html', context)

@staff_member_required
@login_required(login_url='/compte/login')
def modifier_velo(request, pk):
    velo = Velo.objects.get(vel_id=pk)
    formVelo = Velosform_modifier(instance=velo)
    if request.method == 'POST':
        formVelo = Velosform_modifier(request.POST, instance=velo)
        if formVelo.is_valid():
            formVelo.save()
            return redirect('/stock_velos')

    context = {
        'formVelo': formVelo
    }
    return render(request, 'stock_velos/ajouter_velos.html', context)

@staff_member_required
@login_required(login_url='/compte/login')
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

@staff_member_required
@login_required(login_url='/compte/login')
def details_velo(request, num):
    velo = Velo.objects.get(vel_num=num)

    context = {
        'velo': velo,
    }

    return render(request, 'stock_velos/detailsVelo.html', context)


@login_required(login_url='/compte/login')
def details_veloClient(request, num):
    velo = Velo.objects.get(vel_num=num)
    messageDescriptionVelo = f"Il n'y a pas de remarque"
    if velo.vel_remarque is not "" :
        messageDescriptionVelo = velo.vel_remarque

    context = {
        'velo' : velo,
        'messageDescriptionVelo' : messageDescriptionVelo,
    }

    return render(request, 'stock_velos/detailsVeloClient.html', context)