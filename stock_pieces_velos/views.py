from django.shortcuts import render
from .models import PieceDeVelo
from django.contrib.auth.decorators import login_required


@login_required(login_url='/compte/login')
def stock_pieces_velos(request):
    pieces_objets = PieceDeVelo.objects.all()

    context = {
        'piecesObjets': pieces_objets
    }

    return render(request, 'stock_pieces_velos/stock_pieces_velos.html', context)
