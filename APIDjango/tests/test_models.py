# from django.test import TestCase
# from django.utils import timezone
# from api.models import Usuario, Especialidad, Sexo
# from django.contrib.auth import get_user_model

# class CreacionRegistrosTests(TestCase):

#     def test_crear_especialidad(self):
#         # Crear una especialidad
#         especialidad = Especialidad.objects.create(nombre='Especialidad de prueba')
#         especialidad1 = Especialidad.objects.create(nombre='Especialidad de prueba')

#         # Verificar que se haya creado correctamente
#         self.assertEqual(especialidad.nombre, 'Especialidad de prueba')
#         self.assertEqual(especialidad1.nombre, 'Especialidad de prueba')

#     def test_crear_sexo(self):
#         # Crear un sexo
#         sexo = Sexo.objects.create(nombre='Masculino')
#         # sexo1 = Sexo.objects.create(nombre='Masculino')

#         # Verificar que se haya creado correctamente
#         self.assertEqual(sexo.nombre, 'Masculino')
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


# import pytest
# from django.db import IntegrityError
# from django.utils import timezone
# from api.models import Especialidad, Sexo, Usuario

# @pytest.mark.django_db
# class TestEspecialidadModel:

#     def test_crear_especialidad(self):
#         especialidad = Especialidad.objects.create(nombre='Especialidad1')
#         assert especialidad.idEspecialidad is not None

#     def test_nombre_unico(self):
#         Especialidad.objects.create(nombre='Especialidad2')
#         with pytest.raises(IntegrityError):
#             Especialidad.objects.create(nombre='Especialidad2')

#     def test_str_representation(self):
#         especialidad = Especialidad.objects.create(nombre='Especialidad3')
#         assert str(especialidad) == 'Especialidad3'


# @pytest.mark.django_db
# class TestSexoModel:

#     def test_crear_sexo(self):
#         sexo = Sexo.objects.create(nombre='Masculino')
#         assert sexo.idSexo is not None

#     def test_nombre_unico(self):
#         Sexo.objects.create(nombre='Femenino')
#         with pytest.raises(IntegrityError):
#             Sexo.objects.create(nombre='Femenino')

#     def test_str_representation(self):
#         sexo = Sexo.objects.create(nombre='Otro')
#         assert str(sexo) == 'Otro'


# @pytest.mark.django_db
# class TestUsuarioModel:

#     def test_crear_usuario(self):
#         especialidad = Especialidad.objects.create(nombre='EspecialidadTest')
#         sexo = Sexo.objects.create(nombre='SexoTest')
#         usuario = Usuario.objects.create(
#             email='test@example.com',
#             nombre='Test',
#             apellido_paterno='Apellido',
#             apellido_materno='Materno',
#             fecha_de_nacimiento=timezone.now(),
#             password='password',
#             especialidad=especialidad,
#             sexo=sexo,
#         )
#         assert usuario.idUsuario is not None

#     def test_email_unico(self):
#         Usuario.objects.create(
#             email='otro@example.com',
#             nombre='Otro',
#             apellido_paterno='Apellido',
#             apellido_materno='Materno',
#             fecha_de_nacimiento=timezone.now(),
#             password='password',
#         )
#         with pytest.raises(IntegrityError):
#             Usuario.objects.create(
#                 email='otro@example.com',
#                 nombre='Otro2',
#                 apellido_paterno='Apellido2',
#                 apellido_materno='Materno2',
#                 fecha_de_nacimiento=timezone.now(),
#                 password='password2',
#             )

#     def test_str_representation(self):
#         usuario = Usuario.objects.create(
#             email='representacion@example.com',
#             nombre='Representacion',
#             apellido_paterno='Apellido',
#             apellido_materno='Materno',
#             fecha_de_nacimiento=timezone.now(),
#             password='password',
#         )
#         assert str(usuario) == 'representacion@example.com'

# En tu archivo de prueba (por ejemplo, tests/test_models_errores.py)

import pytest
from django.db import IntegrityError
from django.utils import timezone
from api.models import Especialidad, Sexo, Usuario  # Reemplaza 'myapp' con el nombre real de tu aplicación

@pytest.mark.django_db
class TestEspecialidadModelErrores:

    def test_nombre_requerido(self):
        with pytest.raises(IntegrityError):
            Especialidad.objects.create()

@pytest.mark.django_db
class TestSexoModelErrores:

    def test_nombre_requerido(self):
        with pytest.raises(IntegrityError):
            Sexo.objects.create()

@pytest.mark.django_db
class TestUsuarioModelErrores:

    def test_email_requerido(self):
        with pytest.raises(IntegrityError):
            Usuario.objects.create(
                nombre='UsuarioSinEmail',
                apellido_paterno='Apellido',
                apellido_materno='Materno',
                fecha_de_nacimiento=timezone.now(),
                password='password',
            )

    def test_especialidad_nula(self):
        with pytest.raises(IntegrityError):
            Usuario.objects.create(
                email='usuario_con_especialidad_nula@example.com',
                nombre='UsuarioConEspecialidadNula',
                apellido_paterno='Apellido',
                apellido_materno='Materno',
                fecha_de_nacimiento=timezone.now(),
                password='password',
                especialidad=None,
                sexo=None,
            )
