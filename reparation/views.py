from django.shortcuts import render
from .forms import * #EventForm  (A modifier / supprimer)

def reparation(request):
    return render(request, 'reparations/reparations.html')

def reparationsDetails(request):
    nb_perso_max = 3
    nbperso_9h00 = 0
    nbperso_9h30 = 0
    nbperso_9h45 = 0
    nbperso_10h00 = 0
    nbperso_10h30 = 0
    nbperso_10h45 = 0
    nbperso_11h00 = 0
    nbperso_11h30 = 0
    nbperso_11h45 = 0
    nbperso_12h00 = 0
    nbperso_12h30 = 0
    nbperso_12h45 = 0
    nbperso_13h00 = 0
    nbperso_13h30 = 0
    nbperso_13h45 = 0
    nbperso_14h00 = 0
    nbperso_14h30 = 0
    nbperso_14h45 = 0
    nbperso_15h00 = 0
    nbperso_15h30 = 0
    nbperso_16h15 = 0
    nbperso_17h00 = 0

    if request.method == 'POST':
        nbperso_9h00 += 1
        return render(request, 'reparations/reparations.html')






