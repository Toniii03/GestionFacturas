from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente,Factura,Pagos,ArticuloFactura,Usuario

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'birth_date')}),
    )   

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(ArticuloFactura)
admin.site.register(Pagos)
