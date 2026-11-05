from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import LugarPatrimonial, Categoria
from .forms import LugarForm

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

@login_required
def gestion(request):
    lugares = LugarPatrimonial.objects.select_related('categoria').all()
    return render(request, 'catalogo/gestion.html', {'lugares': lugares})

@login_required
@permission_required('fundacionPatrimonio.add_lugarpatrimonial', raise_exception=True)
def agregar_lugar(request):
    form = LugarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestion')
    return render(request, 'catalogo/form_lugar.html', {'form': form, 'titulo': 'Agregar lugar'})

@login_required
@permission_required('fundacionPatrimonio.change_lugarpatrimonial', raise_exception=True)
def editar_lugar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    form = LugarForm(request.POST or None, instance=lugar)
    if form.is_valid():
        form.save()
        return redirect('gestion')
    return render(request, 'catalogo/form_lugar.html', {'form': form, 'titulo': 'Modificar lugar'})