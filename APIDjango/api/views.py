from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Especialidad, Usuario
from django.contrib import messages

# Create your views here.
class Login(APIView):
    template_name='login.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Signup(APIView):
    template_name='signup.html'
    def get(self,request):
        especialidadesListadas = Especialidad.objects.all()
        return render(request,self.template_name, {"especialidades": especialidadesListadas})
    
class Index(APIView):
    template_name='index.html'
    def get(self,request):
        messages.success(request, '¡Sesión iniciada!'),
        return render(request,self.template_name)
    
def registrarUsuario(request):
    nombre = request.POST['txtNombre']
    aPaterno = request.POST['txtAPaterno']
    aMaterno = request.POST['txtAMaterno']
    nacimiento = request.POST['txtNacimiento']
    especialidad = request.POST['cbxEspecialidad']
    email = request.POST['txtEmail']
    password = request.POST['txtContraseña']

    curso = Usuario.objects.create(nombre=nombre, aPaterno=aPaterno, aMaterno=aMaterno, nacimiento=nacimiento, email=email, password=password, especialidad=especialidad)
    messages.success(request, '¡Registro exitoso! En breve te llegará un correo de confirmación')
    return redirect('/')