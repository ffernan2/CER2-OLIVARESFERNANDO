from django.contrib import admin
from .models import Categoria, LugarPatrimonial

admin.site.register(Categoria)

# Register your models here.
class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display=('nombre', 'categoria', 'anio_construccion')
    list_filter=('categoria',)
    search_fields=('nombre', 'ubicacion')

admin.site.register(LugarPatrimonial, LugarPatrimonialAdmin)