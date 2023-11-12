from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Especialidad, Usuario, Sexo
from django.contrib import messages
from django.db.models import Count

from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

# Create your views here.
class Login(APIView):
    template_name='login.html'
    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        email = request.POST['txtEmail']
        password =request.POST['txtPassword']

        user = authenticate(request, email=email, password=password, backend='api.backends.UsuarioBackend')

        if user is not None:
            messages.success(request, '¡Bienvenido! Sesión iniciada.')
            login(request, user)
            return redirect('index')    
        else:
            messages.error(request, 'Usuario o contraseña incorrecto. Por favor, inténtalo de nuevo.')
            return self.get(request)
            
    
class Signup(APIView):
    template_name='signup.html'
    def get(self,request):
        especialidadesListadas = Especialidad.objects.all()
        sexosListados = Sexo.objects.all()
        return render(request,self.template_name, {"especialidades": especialidadesListadas, "sexos": sexosListados})
    
    def post(self,request):
        if request.POST["txtContraseña"] == request.POST["txtContraseña1"]:
            try:
                nombre = request.POST['txtNombre']
                aPaterno = request.POST['txtAPaterno']
                aMaterno = request.POST['txtAMaterno']
                nacimiento = request.POST['txtNacimiento']
                idEspecialidad = request.POST['cbxEspecialidad']
                idSexo = request.POST['cbxSexo']
                email = request.POST['txtEmail']
                password = request.POST['txtContraseña']

                especialidad = Especialidad.objects.get(pk=idEspecialidad)
                sexo = Sexo.objects.get(pk=idSexo)

                user = Usuario.objects.create(email=email, nombre=nombre, aPaterno=aPaterno, aMaterno=aMaterno, nacimiento=nacimiento, password=password, especialidad=especialidad, sexo=sexo)

                user.save()
                confirmation_mail = create_mail(
                    email,
                    'Correo de confirmación',
                    'mails/confirmation.html',
                    {
                        'nombre': nombre
                    }
                )
                confirmation_mail.send(fail_silently=False)
                messages.success(request, '¡Registro exitoso! En breve te llegará un correo de confirmación')
            except IntegrityError:
                messages.error(request, 'El correo ya ha sido utilizado.')

            return self.get(request)    
        
    
class Index(APIView):
    template_name='index.html'
    def get(self,request):
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
        return render(request,self.template_name, {
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

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        
        user = authenticate(request, email=request.POST['txtEmail'], password=request.POST['txtPassword'])

        if user is not None:
           messages.error(request, 'Usuario o contraseña incorrecto. Por favor, inténtalo de nuevo.')
        #    return redirect(request, 'login.html')
               
        else: 
            messages.success(request, '¡Bienvenido! Sesión iniciada.')
            login(request, user)
            return redirect('index')
               
            # return redirect('index.html')
    # return render(request, 'login.html')

def registrarUsuario(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    elif request.POST["txtContraseña"] == request.POST["txtContraseña1"]:
        try:
            nombre = request.POST['txtNombre']
            aPaterno = request.POST['txtAPaterno']
            aMaterno = request.POST['txtAMaterno']
            nacimiento = request.POST['txtNacimiento']
            idEspecialidad = request.POST['cbxEspecialidad']
            email = request.POST['txtEmail']
            password = request.POST['txtContraseña']

            especialidad = Especialidad.objects.get(pk=idEspecialidad)

            user = Usuario.objects.create(nombre=nombre, aPaterno=aPaterno, aMaterno=aMaterno, nacimiento=nacimiento, email=email, password=password, especialidad=especialidad)

            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            confirmation_mail = create_mail(
                email,
                'Correo de confirmación',
                'mails/confirmation.html',
                {
                    'nombre': nombre
                }
            )
            confirmation_mail.send(fail_silently=False)
            messages.success(request, '¡Registro exitoso! En breve te llegará un correo de confirmación')
        except IntegrityError:
            messages.success(request, 'El correo ya ha sido utilizado.')
    
    return render(request, 'signup.html')

def grafica_usuarios_especialidad(request):
    especialidades = Especialidad.objects.annotate(total_usuarios=Count('usuario'))

    labels = [especialidad.nombre for especialidad in especialidades]
    valores = [especialidad.total_usuarios for especialidad in especialidades]

    return render(request, 'tu_app/grafica_usuarios_especialidad.html', {'labels': labels, 'valores': valores})