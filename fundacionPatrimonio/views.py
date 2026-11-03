from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial, Categoria

# Create your views here.
def index(request):
    return render(request, 'catalogo/index.html')

def catalogo_view(request):
    lugares=LugarPatrimonial.objects.all()
    return render(request, 'catalogo/catalogo.html', {'lugares': lugares})

def detalle_lugar(request, id):
    lugar=get_object_or_404(LugarPatrimonial, id=id)
    return render(request, 'catalogo/detalle.html', {'lugar' : lugar})

