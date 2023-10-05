from api.models import Especialidad  

def agregar_especialidades():
    especialidades = ['Programador', 'Diseñador Gráfico']

    for nombre_especialidad in especialidades:
        especialidad = Especialidad(nombre=nombre_especialidad)
        especialidad.save()

if __name__ == "__main__":
    agregar_especialidades()
