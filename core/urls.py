from django.urls import path
from .views import index, produtos, cliente, new_cliente, cliente_update, cliente_detail, cliente_delete
from .views import new_produto, update_produto, delete_produto

urlpatterns = [
    path('index', index, name='index'),
    path('', cliente, name='cliente'),
    path('new_cliente', new_cliente, name='new_cliente'),
    path('detail_cliente/<int:id>/', cliente_detail, name='detail_cliente'),
    path('update_cliente/<int:id>/', cliente_update, name='update_cliente'),
    path('delete_cliente/<int:id>/', cliente_delete, name='delete_cliente'),
    path('new_produto', new_produto, name='new_produto'),
    path('produto', produtos, name='produto'),
    path('update_produto/<int:id>/', update_produto, name='update_produto'),
    path('delete_produto/<int:id>/', delete_produto, name='delete_produto'),

]
