import json
from urllib import request
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib import messages

# Create your views here.

def obtenerDatos(request):
    datos = list(Articulo.objects.values());
    return JsonResponse({'datosBBDD': datos}, safe=False)

def vistaPrincipal(request):
    return render (request,'gestFacturas/principal.html')

class Registrousuario(CreateView):
    model = Usuario
    form_class = form_registroUsuarios
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request,'Cliente creado correctamente')
        form.instance.usuario = self.request.user
        form.save();
        return super().form_valid(form)

class vistaLogin(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('principal')   
    
    def form_invalid(self, form):
        messages.error(self.request,'El nombre de usuario o la contraseña que ingresaste no son correctos. Por favor, inténtalo de nuevo')
        return super().form_invalid(form)

class Clientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "gestFacturas/clientes.html"
    context_object_name = 'clientes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clientes = Cliente.objects.all().order_by('nombre')
        context["clientesOrdenados"] = clientes.filter(usuario = self.request.user)
        return context
    
    
    
class Cliente_detalles(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = "gestFacturas/cliente_detalles.html"
    context_object_name = "cliente"
    
    def get_context_data(self, **kwargs):
        cliente = get_object_or_404(Cliente,pk=self.object.pk)
        context = super().get_context_data(**kwargs)
        context["facturasCliente"] = Factura.objects.filter(cliente=cliente)
        return context

class Cliente_aniadir(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = "gestFacturas/cliente_crear.html"
    form_class = form_Cliente
    success_url= reverse_lazy('clientes')
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente creado correctamente')
        referer_url = self.request.META.get('HTTP_REFERER') #URL de la pagina anterior de la que venga el USER
        form.instance.usuario = self.request.user
        form.save()
        
        #si la pagina anterior es la ulr /cliente/new redirige a clientes
        if referer_url and "cliente/new" in referer_url:
            return redirect(reverse_lazy('clientes'))
        
        return redirect(referer_url)
    
class Cliente_aniadir_modal(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = "modales/CrearCliente.html"
    form_class = form_Cliente
    success_url = reverse_lazy('facturas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        cliente = form.save()
        messages.success(self.request, 'Cliente creado correctamente')
        return super().form_valid(form)
    


    def get_success_url(self):
        return reverse_lazy('facturas')

class Cliente_eliminar(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'gestFacturas/borrar.html'
    context_object_name = 'objeto'
    success_url= reverse_lazy('clientes')
    
    def form_valid(self, form):
        messages.success(self.request,'Cliente eliminado correctamente')
        return super().form_valid(form)

class Cliente_editar(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "gestFacturas/cliente_editar.html"
    form_class = form_Cliente
    pk_url_kwarg='pk'
    
    def get_success_url(self):
        return reverse_lazy('cliente_detalles', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request,'Cliente actualizado correctamente')
        return super().form_valid(form)
    
class Empresas_listar(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = "empresas/empresas_listar.html"
    context_object_name = 'empresas'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(usuario = self.request.user)
        print(query)

        return query

class Empresas_aniadir(LoginRequiredMixin, CreateView):
    model = Empresa
    template_name = "empresas/empresa_crear.html"
    form_class = form_empresa
    success_url = reverse_lazy('empresas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request,'Empresa creada correctamente')
        referer_url = self.request.META.get('HTTP_REFERER') #URL de la pagina anterior de la que venga el USER
        form.save()
        
        #si la pagina anterior es la ulr /empresas/new redirige a empresas
        if referer_url and "empresas/new" in referer_url:
            return redirect(reverse_lazy('empresas'))
        
        # Si no es la página específica, redirige a la página anterior
        return redirect(referer_url)
    
class Empresas_detalles(LoginRequiredMixin, DetailView):
    model = Empresa
    template_name = 'empresas/empresa_detalles.html'
    context_object_name = "empresa"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["facturasCliente"] = Factura.objects.filter(hechaPor=self.get_object())
        return context
    
class Empresa_eliminar(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'gestFacturas/borrar.html'
    context_object_name = 'objeto'
    success_url= reverse_lazy('empresas')
    
class Empresa_editar(LoginRequiredMixin, UpdateView):
    model = Empresa
    template_name = 'empresas/empresa_editar.html'
    form_class = form_empresa
    success_url = reverse_lazy('empresas')
    
    def form_valid(self, form):
        messages.success(self.request,'Empresa Actualizada correctamente')
        return super().form_valid(form)
    
class Empresa_aniadir_modal(LoginRequiredMixin, CreateView):
    model = Empresa
    template_name = "modales/CrearEmpresa.html"
    form_class = form_empresa
    success_url = reverse_lazy('facturas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        empresa = form.save()
        messages.success(self.request, 'Empresa Creada correctamente')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('facturas')

class Facturas(LoginRequiredMixin,ListView):
    model=Factura
    template_name = "gestFacturas/facturas.html"
    context_object_name = 'facturas'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(usuario = self.request.user)

        orden = self.request.GET.get('orden')
        direccion = self.request.GET.get('direccion')

        if not orden:
            orden = 'hechaPor'

        if orden:
            if direccion == "asc":
                query = query.order_by(orden)
            else:
                query = query.order_by(f'-{orden}')
        return query
    
class Factura_detalle(LoginRequiredMixin, DetailView):
    model=Factura
    
@login_required
def Factura_crear(request):    
    if request.method == 'POST':
        articulos_data = request.POST.get('articulos_data')
        presupuesto_form = form_Factura(request.POST,usuario=request.user)

        if articulos_data:
            articulosDeLaFactura = json.loads(articulos_data)
            if presupuesto_form.is_valid():
                factura = presupuesto_form.save(commit=False)
                factura.usuario = request.user
                factura.save()
                #Guardar cada articulo con su factura
                for articulo, datos in articulosDeLaFactura.items():
                    cantidad, precio = datos
                    
                    ArticuloFactura.objects.create(
                        factura=factura,
                        articulo=articulo,
                        cantidad=cantidad,
                        precio_unitario=precio
                    )
                
                Pagos.objects.create(
                    factura=factura,
                    pagado=0,
                    total_pagar=factura.total,
                    fecha_pago=factura.fecha_vencimiento,
                    usuario=factura.usuario,
                    metodo_pago=factura.metodo_pago
                )
                messages.success(request,'Factura creada correctamente')
                return redirect('facturas')
    else:
        presupuesto_form = form_Factura(usuario=request.user)
    return render(request, 'gestFacturas/crear_factura.html', {
        'form': presupuesto_form,})


class Factura_editar(LoginRequiredMixin, UpdateView):
    model = Factura
    template_name = "gestFacturas/editar_factura.html"
    form_class = form_Factura
    pk_url_kwarg='pk'
    success_url= reverse_lazy('facturas')

    def get_form_kwargs(self): #sobreescritura de metodo para pasarle el usuario de donde tiene que coger los select
        kwargs = super().get_form_kwargs() 
        kwargs['usuario'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        messages.success(self.request,'Factura actualizada correctamente')
        ArticuloFactura.objects.filter(factura=self.kwargs['pk']).delete()
        articulos_data = self.request.POST.get('articulos_data')
        listaArticulos = json.loads(articulos_data)
        factura = Factura.objects.get(pk=self.kwargs['pk'])

        for articulo in listaArticulos:
            ArticuloFactura.objects.create(
                factura=factura,
                articulo=articulo['articulo'],
                cantidad=articulo['cantidad'],
                precio_unitario=articulo['precio_unitario']
            )
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        factura = Factura.objects.get(pk=self.kwargs['pk'])
        context["hechaPor"] = factura

        listaArticulos = [
            {
                "id": art.id,
                "articulo": art.articulo,
                "cantidad": art.cantidad,
                "precio_unitario": float(art.precio_unitario),
            }
            for art in ArticuloFactura.objects.filter(factura=factura)
        ]
        context["listaArticulos_json"] = json.dumps(listaArticulos)

        ArticuloFactura.objects.filter(factura=self.kwargs['pk'])
        context["listaArticulos"] = listaArticulos

        return context

class Factura_eliminar(LoginRequiredMixin, DeleteView):
    model = Factura
    template_name = 'gestFacturas/borrar.html'
    context_object_name = 'objeto'
    success_url= reverse_lazy('facturas')

    def form_valid(self, form):
        messages.success(self.request,'Factura eliminada correctamente')
        return super().form_valid(form)
    
class pagos(LoginRequiredMixin,ListView):
    model = Pagos;
    template_name = 'pagos/pagos_listado.html'
    context_object_name = 'pagos'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(usuario = self.request.user)

        orden = self.request.GET.get('orden')
        direccion = self.request.GET.get('direccion')

        if not orden:
            orden = 'fecha_pago'

        if orden:
            if direccion == "asc":
                query = query.order_by(orden)
            else:
                query = query.order_by(f'-{orden}')
        return query
    
    
class pagos_eliminar(LoginRequiredMixin, DeleteView):
    model = Pagos
    template_name = 'gestFacturas/borrar.html'
    context_object_name = 'objeto'
    success_url= reverse_lazy('pagos')
    
    def form_valid(self, form):
        messages.success(self.request,'Pago eliminado correctamente')
        return super().form_valid(form)
    
class pagos_editar(LoginRequiredMixin, UpdateView):
    model = Pagos
    template_name = "pagos/pago_editar.html"
    form_class = form_Pagos
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('pagos')

    def form_valid(self, form):
        messages.success(self.request, 'Pago actualizado correctamente')
        return super().form_valid(form)
    