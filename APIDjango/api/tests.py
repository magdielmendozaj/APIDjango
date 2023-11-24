from django.test import TestCase
from .models import Usuario, Especialidad, Sexo

class UsuarioModelTest(TestCase):

    def setUp(self):
        especialidad = Especialidad.objects.create(nombre='Programación')
        sexo = Sexo.objects.create(nombre='Hombre')
        Usuario.objects.create(
            email='test@example.com',
            nombre='John',
            apellido_paterno='Doe',
            apellido_materno='Smith',
            fecha_de_nacimiento='2000-01-01',
            password='password',
            especialidad=especialidad,
            sexo=sexo,
        )

    # Prueba correcta: Comprobar si el nombre completo es correcto
    def test_get_full_name_correcto(self):
        user = Usuario.objects.get(email='test@example.com')
        self.assertEqual(user.get_full_name(), 'John Doe Smith')

    # Prueba correcta: Comprobar si la edad del usuario es menor de 18 años
    def test_edad_menor_18_correcto(self):
        user = Usuario.objects.get(email='test@example.com')
        self.assertTrue(user.edad_menor_18())

    # Prueba errónea: Intentar crear un usuario sin email
    def test_create_user_sin_email_erroneo(self):
        with self.assertRaises(ValueError):
            Usuario.objects.create_user(email='', password='password')

    # Prueba errónea: Intentar crear un superusuario sin nombre
    def test_create_superuser_sin_nombre_erroneo(self):
        with self.assertRaises(ValueError):
            Usuario.objects.create_superuser(email='admin@example.com', password='password', nombre='')