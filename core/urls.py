from django.urls import path
from .views import index, produto, cliente, new_cliente, cliente_update, cliente_detail, cliente_delete


urlpatterns = [
    path('', index, name='index'),
    path('produto', produto, name='produto'),
    path('cliente', cliente, name='cliente'),
    path('new_cliente', new_cliente, name='new_cliente'),
    path('detail_cliente/<int:id>/', cliente_detail, name='detail_cliente'),
    path('update_cliente/<int:id>/', cliente_update, name='update_cliente'),
    path('delete_cliente/<int:id>/', cliente_delete, name='delete_cliente'),

]
