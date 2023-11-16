from django.contrib.auth.hashers import check_password
from .models import Usuario

class UsuarioBackend:
    def authenticate(email=None, password=None):
        print(f'Trying to authenticate user with email: {email}')
        try:
            alumno = Usuario.objects.get(email=email)
            if check_password(password, alumno.password):
                print('Authentication successful')
                return alumno
            else:
                print('Authentication failed: Incorrect password')
        except Usuario.DoesNotExist:
            print('Authentication failed: User not found')
            return None

    def get_user(self, matricula):
        try:
            return Usuario.objects.get(pk=matricula)
        except Usuario.DoesNotExist:
            return None