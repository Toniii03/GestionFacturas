from datetime import date
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    cif = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Factura(models.Model):
    METODOS_PAGO = [
        ('tarjeta', 'Tarjeta de Crédito/Débito'),
        ('transferencia', 'Transferencia Bancaria'),
        ('efectivo', 'Efectivo'),
    ]
    
    ESTADOS = [
    ('pendiente', 'Pendiente'),
    ('pagada', 'Pagada'),
    ('anulada', 'Anulada'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    hechaPor = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now=False, auto_now_add=False,default=date.today)
    fecha_vencimiento = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
    metodo_pago = models.CharField(max_length=15, choices=METODOS_PAGO, default='efectivo')
    estado = models.CharField(max_length=10,choices=ESTADOS, default='pendiente')
    notas = models.TextField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    impuesto = models.DecimalField(max_digits=12, decimal_places=2,default=21)
    descuento = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2,default=0)

    
    def clean(self):
        if (self.fecha_emision > date.today()):
            raise ValidationError("La fecha no puede ser futura")
        return super().clean()
    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        
    def __str__(self):
        return f"Factura {self.id} {self.cliente}"

class ArticuloFactura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    articulo = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.factura.pk} - articulo {self.articulo}"
    
class Pagos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    pagado = models.DecimalField(max_digits=12, decimal_places=2)
    total_pagar = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pago = models.DateTimeField()
    metodo_pago = models.CharField(max_length=15, choices=Factura.METODOS_PAGO)

    def __str__(self):
        return f"Pago {self.id} - {self.factura.hechaPor}"
    