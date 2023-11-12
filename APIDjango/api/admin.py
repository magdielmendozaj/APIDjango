from django.contrib import admin
from .models import Usuario, Especialidad, Sexo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(Sexo)