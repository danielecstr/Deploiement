from django.shortcuts import render
from .models import Local
from django.contrib.auth.decorators import login_required


@login_required(login_url='/compte/login')
def stock_locaux(request):
    local_objets = Local.objects.all()

    context = {
        'localObjets': local_objets
    }

    return render(request, 'stock_locaux/stock_locaux.html', context)
