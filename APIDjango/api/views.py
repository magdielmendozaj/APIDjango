from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Especialidad, Usuario, Sexo
from django.contrib import messages
from django.db.models import Count

from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

from allauth.socialaccount.models import SocialAccount

import os
import requests
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, '¡Bienvenido! Sesión iniciada.')
                return redirect('index')
            else:
                messages.error(request, 'Error, usuario o contraseña incorrecto.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            confirmation_mail = create_mail(
                    email,
                    'Correo de confirmación',
                    'mails/confirmation.html',
                    {
                        'nombre': nombre,
                    }
                )
            try:
                confirmation_mail.send(fail_silently=False)
            except Exception as e:
                print(f"Error al enviar correo de confirmación: {e}")
                messages.warning(request, 'Hubo un problema al enviar el correo de confirmación.')
            form.save()
            messages.success(request, '¡Registro exitoso! En breve te llegará un correo de confirmación.')
            return redirect('login')
        else: 
            print(f"Errores en el formulario: {form.errors}")
            messages.error(request, 'Hubo un problema al procesar el formulario. Por favor, revisa los errores.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})   

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def index_view(request):
    especialidades = Especialidad.objects.annotate(total_usuarios=Count('usuario'))

    # Obtén datos para el gráfico de barras
    labels_barras = [especialidad.nombre for especialidad in especialidades]
    valores_barras = [especialidad.total_usuarios for especialidad in especialidades]

    # Obtén datos para el gráfico circular
    labels_circular = labels_barras
    valores_circular = valores_barras

    # Obtén datos para el gráfico de líneas (puedes utilizar fechas si tienes registros de fechas)
    labels_lineas = [str(especialidad) for especialidad in especialidades]
    valores_lineas = valores_barras
    return render(request,'index.html', {
        'labels_barras': labels_barras,
        'valores_barras': valores_barras,
        'labels_circular': labels_circular,
        'valores_circular': valores_circular,
        'labels_lineas': labels_lineas,
        'valores_lineas': valores_lineas,
    })
    
def create_mail(email, subject, template_path, context):
    template = get_template(template_path)
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject = subject,
        body = '',
        from_email = settings.EMAIL_HOST_USER,
        to = {
            email
        },
        cc = []
    )
    mail.attach_alternative(content, 'text/html')
    return mail

def grafica_usuarios_especialidad(request):
    especialidades = Especialidad.objects.annotate(total_usuarios=Count('usuario'))

    labels = [especialidad.nombre for especialidad in especialidades]
    valores = [especialidad.total_usuarios for especialidad in especialidades]

    return render(request, 'tu_app/grafica_usuarios_especialidad.html', {'labels': labels, 'valores': valores})

# def github_login_callback(request):
#     # Manejar la lógica de redirección después de iniciar sesión con GitHub
#     # ...

#     # Obtener la cuenta social de GitHub asociada con el usuario
#     github_social_account = SocialAccount.objects.filter(provider='github', user=request.user).first()

#     if github_social_account:
#         # El usuario ya tiene una cuenta de GitHub vinculada, puedes redirigirlo a donde desees
#         return redirect('index')
#     else:
#         # El usuario no tiene una cuenta de GitHub vinculada, puedes manejar la lógica de vinculación aquí
#         # ...

#         # Obtener los datos relevantes de la cuenta de GitHub
#         github_username = github_social_account.extra_data.get('login')
#         github_access_token = github_social_account.socialtoken_set.first().token

#         # Crear o actualizar el usuario con los datos de GitHub
#         usuario, created = Usuario.objects.get_or_create(email=request.user.email)

#         # Actualizar los campos específicos de GitHub
#         usuario.github_username = github_username
#         usuario.github_access_token = github_access_token

#         # Puedes agregar otros campos de usuario que desees actualizar
#         # usuario.otro_campo = valor

#         usuario.save()

#         # Redirigir a donde desees después de la vinculación
#         return redirect('index')
    
# def my_custom_view(request):
#     # Redirigir al usuario a la página de inicio de sesión social de GitHub
#     return redirect('socialaccount_login', 'github')

# def handle_github_callback(request):
#     # Manejar la lógica después del inicio de sesión con GitHub
#     github_social_account = SocialAccount.objects.filter(provider='github', user=request.user).first()

#     if github_social_account:
#         # El usuario ya tiene una cuenta de GitHub vinculada, puedes redirigirlo a donde desees
#         return redirect('tu_página_principal')
#     else:
#         # El usuario no tiene una cuenta de GitHub vinculada, puedes manejar la lógica de vinculación aquí
#         return redirect('página_de_vinculación_de_cuentas_github')

User = get_user_model()

class GitHubLogin(View):
    def get(self, request):
        github_authorize_url = f'https://github.com/login/oauth/authorize?client_id={settings.GITHUB_CLIENT_ID}&redirect_uri={settings.GITHUB_REDIRECT_URI}&scope=user'
        return redirect(github_authorize_url)

class GitHubCallback(View):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return HttpResponse("Error: No se proporcionó el código de autorización.")

        # Obtener el token de acceso usando el código de autorización
        response = requests.post(
            'https://github.com/login/oauth/access_token',
            params={
                'client_id': settings.GITHUB_CLIENT_ID,
                'client_secret': settings.GITHUB_CLIENT_SECRET,
                'code': code,
            },
            headers={'Accept': 'application/json'}
        )
        data = response.json()

        # Obtener detalles del usuario
        user_response = requests.get(
            'https://api.github.com/user',
            headers={'Authorization': f"Bearer {data['access_token']}"}
        )
        user_data = user_response.json()

        # Crear o actualizar el usuario en la base de datos
        user, created = User.objects.get_or_create(github_username=user_data['login'])
        user.github_access_token = data['access_token']
        user.save()

        # Redirigir a la página principal u otra página después de la autenticación
        return redirect(reverse('index'))