from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial, Categoria

# Create your views here.
# RF01
def index(request):
    return render(request, 'catalogo/index.html')

# RF02
def catalogo_view(request):
    lugares=LugarPatrimonial.objects.all()
    categorias=Categoria.objects.all()
    return render(request, 'catalogo/catalogo.html', {'lugares': lugares, 'categorias': categorias})

# RF03
def detalle_lugar(request, id):
    lugar=get_object_or_404(LugarPatrimonial, id=id)
    return render(request, 'catalogo/detalle.html', {'lugar' : lugar})

# RF05
def filtro_categoria(request, id):
    categoria_seleccionada=get_object_or_404(Categoria, id=id)
    lugares=LugarPatrimonial.objects.filter(categoria=categoria_seleccionada)
    categorias=Categoria.objects.all()
    return render(request, 'catalogo/catalogo.html', {'lugares': lugares, 'categorias': categorias, 'categoria_seleccionada': categoria_seleccionada})