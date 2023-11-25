from django.test import TestCase
from django.utils import timezone
from api.models import Usuario, Especialidad, Sexo
from django.contrib.auth import get_user_model

class CreacionRegistrosTests(TestCase):

    def test_crear_especialidad(self):
        # Crear una especialidad
        especialidad = Especialidad.objects.create(nombre='Especialidad de prueba')
        especialidad1 = Especialidad.objects.create(nombre='Especialidad de prueba')

        # Verificar que se haya creado correctamente
        self.assertEqual(especialidad.nombre, 'Especialidad de prueba')
        self.assertEqual(especialidad1.nombre, 'Especialidad de prueba')

    def test_crear_sexo(self):
        # Crear un sexo
        sexo = Sexo.objects.create(nombre='Masculino')
        # sexo1 = Sexo.objects.create(nombre='Masculino')

        # Verificar que se haya creado correctamente
        self.assertEqual(sexo.nombre, 'Masculino')
        # self.assertEqual(sexo1.nombre, 'Masculino')

    # def test_crear_usuario(self):
    #     # Configurar datos de prueba
    #     especialidad = Especialidad.objects.create(nombre='Especialidad de prueba')
    #     sexo = Sexo.objects.create(nombre='Masculino')
    #     user_data = {
    #         'email': 'testuser@example.com',
    #         'nombre': 'John',
    #         'apellido_paterno': 'Doe',
    #         'apellido_materno': 'Smith',
    #         'fecha_de_nacimiento': timezone.now().date(),
    #         'password': 'testpassword',
    #         'especialidad': especialidad,
    #         'sexo': sexo,
    #     }

    #     # Crear un usuario
    #     user = get_user_model().objects.create_user(**user_data)

    #     # Verificar que se haya creado correctamente
    #     self.assertEqual(user.email, 'testuser@example.com')
    #     self.assertEqual(user.get_full_name(), 'John Doe Smith')
    #     self.assertTrue(user.check_password('testpassword'))
    #     self.assertEqual(user.especialidad, especialidad)
    #     self.assertEqual(user.sexo, sexo)
    #     self.assertFalse(user.is_staff)
    #     self.assertFalse(user.is_superuser)
    #     self.assertTrue(user.is_active)

