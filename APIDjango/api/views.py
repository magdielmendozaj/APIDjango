from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib import messages

# Create your views here.
class Home(APIView):
    template_name='index.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Registro(APIView):
    template_name='registro.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Inicio(APIView):
    template_name='inicio.html'
    def get(self,request):
        messages.success(request, '¡Sesión iniciada!'),
        return render(request,self.template_name)