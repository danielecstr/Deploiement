"""
Auteur : Daniele Castro
"""
from django.db.models.functions import ExtractMonth
from django.shortcuts import render
from .models import Location_Velo
from .models import Velo


def statistique(request):
    locations = Location_Velo.objects.all()
    stats = []
    nbJanv = 0
    nbFev = 0
    nbMars = 0
    nbAvr = 0
    nbMai = 0
    nbJuin = 0
    nbJuillet = 0
    nbAou = 0
    nbSep = 0
    nbOct = 0
    nbNov = 0
    nbDec = 0

    for l in locations:

        if l.date_debut.strftime('%B') == "January":
            nbJanv +=1
        elif l.date_debut.strftime('%B') == "February":
            nbFev +=1
        elif l.date_debut.strftime('%B') == "March":
            nbMars +=1
        elif l.date_debut.strftime('%B') == "April":
            nbAvr +=1
        elif l.date_debut.strftime('%B') == "May":
            nbMai +=1
        elif l.date_debut.strftime('%B') == "June":
            nbJuin +=1
        elif l.date_debut.strftime('%B') == "July":
            nbJuillet +=1
        elif l.date_debut.strftime('%B') == "August":
            nbAou +=1
        elif l.date_debut.strftime('%B') == "September":
            nbSep +=1
        elif l.date_debut.strftime('%B') == "October":
            nbOct +=1
        elif l.date_debut.strftime('%B') == "November":
            nbNov +=1
        elif l.date_debut.strftime('%B') == "December":
            nbDec +=1


    stats=[nbJanv,
    nbFev,
    nbMars,
    nbAvr,
    nbMai,
    nbJuin,
    nbJuillet,
    nbAou,
    nbSep,
    nbOct,
    nbNov,
    nbDec,]

    typeVelo = [['Type', 'Nombre de type']]

    velos = Velo.objects.all()

    # c = [['Task', 'Hours per Day'],
    #       ['Work',     11],
    #       ['Eat',      2],
    #       ['A',  2],
    #       ['Watch TV', 2],
    #       ['Sleep',    7]]
    type = []
    for velo in velos:
        type.append(velo.vel_type)



    for velo in velos:
        list = [velo.vel_type, type.count(velo.vel_type)]
        if list not in typeVelo:
            typeVelo.append(list)


    context = {
        'stats' : stats,
        'typeVelo' : typeVelo
    }
    return render(request, 'statistique/statistique.html', context)