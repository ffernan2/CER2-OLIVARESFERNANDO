from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial, Categoria

# Create your views here.
def index(request):
    return render(request, 'fundacionPatrimonio/index.html')

def catalogo_view(request):
    lugares=LugarPatrimonial.objects.all()
    return render(request, 'fundacionPatrimonio/catalogo.html', {'lugares': lugares})

def detalle_lugar(request, id):
    lugar=get_object_or_404(LugarPatrimonial, id=id)
    return render(request, 'fundacionPatrimonio/detalle.html', {'lugar' : lugar})

