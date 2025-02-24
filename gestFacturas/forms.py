from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class form_empresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        exclude = ['usuario']

    def save(self, commit=True):
        Empresa = super().save(commit=False)
        Empresa.usuario = self.instance.usuario 
        if commit:
            Empresa.save()
        return Empresa

class form_Factura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        exclude = ['usuario']
        widgets = {
            'fecha_emision': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        usuarioLogin = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

        self.fields['subtotal'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
        #Filtra los campos hechoPor y cliente por el usuario que este logueado
        self.fields['hechaPor'].queryset = Empresa.objects.filter(usuario=usuarioLogin)
        self.fields['cliente'].queryset = Cliente.objects.filter(usuario=usuarioLogin)
        
    
    def save(self, commit=True):
        Factura = super().save(commit=False)
        Factura.usuario = self.instance.usuario 
        if commit:
            Factura.save()
        return Factura
    
class form_registroUsuarios(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()  
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        self.fields['username'].label = 'Nombre de usuario'
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya está en uso')
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1 and len(password1) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        password1 = self.cleaned_data.get("password1")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden. Por favor, asegúrate de escribir la misma contraseña en ambos campos.")
        return password2

class form_ArticuloFactura (forms.ModelForm):
    class Meta:
        model = ArticuloFactura
        fields = '__all__'
        
class form_Cliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['usuario']

    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.usuario = self.instance.usuario 
        if commit:
            cliente.save()
        return cliente
        
class form_Pagos(forms.ModelForm):
    factura_display = forms.CharField(disabled=True, required=False, label="Factura hecha por")
    total_pagar = forms.DecimalField(disabled=True, required=False)
    exclude = ['usuario']

    class Meta:
        model = Pagos
        fields = ['factura', 'fecha_pago', 'pagado', 'total_pagar', 'metodo_pago']
        widgets = {
            'fecha_pago': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'factura': forms.TextInput(attrs={'readonly': 'readonly'}), 
        }

    def save(self, commit=True):
        Pagos = super().save(commit=False)
        Pagos.usuario = self.instance.usuario 
        if commit:
            Pagos.save()
        return Pagos    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.factura:
            self.fields['factura'].initial = self.instance.factura.hechaPor
        if self.instance and self.instance.fecha_pago:
            self.fields['fecha_pago'].initial = self.instance.fecha_pago.strftime('%Y-%m-%d')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total_pagar = instance.total_pagar - instance.pagado
        instance.save()
        return instance
