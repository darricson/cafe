from django.contrib import admin
from .models import Produto, Cliente
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'estado', 'preco', 'estoque')


class CLienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, CLienteAdmin)