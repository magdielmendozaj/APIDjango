from django.contrib import admin
from .models import Usuario, Especialidad, Sexo, Profile

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(Sexo)
admin.site.register(Profile)