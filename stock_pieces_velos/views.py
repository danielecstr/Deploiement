from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PieceDeVelo
from .forms import Piecesform, Piecesform_modifier


@login_required(login_url='/compte/login')
def stock_pieces_velos(request):
    pieces_objets = PieceDeVelo.objects.all()

    context = {
        'piecesObjets': pieces_objets
    }

    return render(request, 'stock_pieces_velos/stock_pieces_velos.html', context)


def nouvelle_piece(request):
    formPiece = Piecesform()
    if request.method == 'POST':
        formVelo = Piecesform(request.POST)
        if formVelo.is_valid():
            if PieceDeVelo.objects.all().count() == 0:
                nb = 1
            else:
                nb = PieceDeVelo.objects.latest('piece_id').piece_num + 1
            velo = PieceDeVelo(piece_num=nb,
                               piece_photo=formVelo.cleaned_data.get('piece_photo'),
                               piece_num_cadre=formVelo.cleaned_data.get('piece_num_cadre'),
                               piece_nom=formVelo.cleaned_data.get('piece_nom'),
                               piece_type=formVelo.cleaned_data.get('piece_type'),
                               piece_marque=formVelo.cleaned_data.get('piece_marque'),
                               piece_type_velo=formVelo.cleaned_data.get('piece_type_velo'),
                               piece_nb=formVelo.cleaned_data.get('piece_nb'),
                               piece_remarque=formVelo.cleaned_data.get('piece_remarque'),
                               fourni_id=formVelo.cleaned_data.get('fourni_id'),
                               local_id=formVelo.cleaned_data.get('local_id'),
                               commande_fourni_id=formVelo.cleaned_data.get('commande_fourni_id'),
                               )
            velo.save()
            return redirect('/stock_pieces_velos')

    context = {
        'formPiece': formPiece
    }
    return render(request, 'stock_pieces_velos/ajouter_piece.html', context)


def supprimer_piece(request, num):
    piece = PieceDeVelo.objects.get(piece_num=num)
    if request.method == 'POST':
        piece.delete()
        return redirect('/stock_pieces_velos')

    context = {
        'item': piece
    }
    return render(request, 'stock_pieces_velos/supprimer_piece.html', context)


def commander_piece(request, num):
    piece = PieceDeVelo.objects.get(piece_num=num)
    if request.method == 'POST':

        return redirect('/stock_pieces_velos')

    context = {
        'item': piece
    }
    return render(request, 'stock_pieces_velos/commander_piece.html', context)


def modifier_piece(request, num):
    piece = PieceDeVelo.objects.get(piece_num=num)
    formPiece = Piecesform_modifier(instance=piece)
    if request.method == 'POST':
        formPiece = Piecesform_modifier(request.POST, instance=piece)
        if formPiece.is_valid():
            formPiece.save()
            return redirect('/stock_pieces_velos')

    context = {
        'formPiece': formPiece
    }
    return render(request, 'stock_pieces_velos/ajouter_piece.html', context)


def details_piece(request, num):
    piece = PieceDeVelo.objects.get(piece_num=num)

    context = {
        'piece': piece,
    }

    return render(request, 'stock_pieces_velos/details_piece.html', context)
