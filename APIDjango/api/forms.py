from django import forms
from django.forms import widgets
from .models import Usuario, Especialidad, Sexo, Profile

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(label='Nombre(s)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido_paterno = forms.CharField(label='Apellido Paterno', widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido_materno = forms.CharField(label='Apellido Materno', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_de_nacimiento = forms.DateField(label='Fecha de nacimiento', widget=widgets.DateInput(attrs={'class': 'form-control','type': 'date'}))
        
    especialidad = forms.ModelChoiceField(label='Selecciona tu especialidad', queryset=Especialidad.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    sexo = forms.ModelChoiceField(label='Selecciona tu sexo', queryset=Sexo.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_de_nacimiento', 'especialidad', 'sexo']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'facebook_username', 'instagram_username', 'twitter_username']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3','placeholder':'Enlace'}),
            'facebook_username': forms.TextInput(attrs={'class':'form-control mt-3','placeholder':'Usuario de Facebook'}),
            'instagram_username': forms.TextInput(attrs={'class':'form-control mt-3','placeholder':'Usuario de Instagram'}),
            'twitter_username': forms.TextInput(attrs={'class':'form-control mt-3','placeholder':'Usuario de Twitter'}),
        }