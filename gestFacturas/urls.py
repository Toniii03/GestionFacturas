from django.urls import path
from gestFacturas import views

urlpatterns = [
    path('login/', views.vistaLogin.as_view(), name='login'),
    path('registro/', views.Registrousuario.as_view(), name='registro'),
    path('', views.Clientes.as_view(), name='principal'),
    path('clientes/', views.Clientes.as_view(), name='clientes'),
    path('cliente/<int:pk>', views.Cliente_detalles.as_view(), name='cliente_detalles'),
    path('cliente/eliminar/<int:pk>', views.Cliente_eliminar.as_view(), name='cliente_eliminar'),
    path('cliente/new', views.Cliente_aniadir.as_view(), name='cliente_añadir'),
    path('cliente/<int:pk>/editar', views.Cliente_editar.as_view(), name='cliente_editar'),
    path('cliente/new/modal', views.Cliente_aniadir_modal.as_view(), name='cliente_añadir_modal'),
    path('empresas/', views.Empresas_listar.as_view(), name='empresas'),
    path('empresas/new', views.Empresas_aniadir.as_view(), name='empresas_añadir'),
    path('empresas/<int:pk>/editar', views.Empresas_detalles.as_view(), name='empresas_detalles'),
    path('empresas/eliminar/<int:pk>', views.Empresa_eliminar.as_view(), name='empresa_eliminar'),
    path('empresas/editar/<int:pk>', views.Empresa_editar.as_view(), name='empresa_editar'),
    path('empresas/new/modal', views.Empresa_aniadir_modal.as_view(), name='empresa_añadir_modal'),
    path('facturas/', views.Facturas.as_view(), name='facturas'),
    path('factura/new', views.Factura_crear, name='factura_nueva'),
    path('factura/editar/<int:pk>', views.Factura_editar.as_view(), name='factura_editar'),
    path('factura/eliminar/<int:pk>', views.Factura_eliminar.as_view(), name='factura_eliminar'),
    path('pagos/', views.pagos.as_view(), name='pagos'),
    path('pagos/eliminar/<int:pk>', views.pagos_eliminar.as_view(), name='pago_eliminar'),
    path('pagos/editar/<int:pk>', views.pagos_editar.as_view(), name='pago_editar'),
    
]