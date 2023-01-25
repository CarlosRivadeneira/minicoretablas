from django.shortcuts import render
from django.db.models import Sum
from .models import Empresa
from django.http import HttpResponse

def listar_empresas(request):
    empresas = Empresa.objects.annotate(total_precio=Sum('productos__precio')).prefetch_related('productos').all()
    return render(request, 'listar_empresas.html', {'empresas': empresas})


def index(request):
    return HttpResponse("Hello, world")