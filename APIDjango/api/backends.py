from .models import Usuario

class UsuarioBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.check_password(password):
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, idUser):
        try:
            return Usuario.objects.get(pk=idUser)
        except Usuario.DoesNotExist:
            return None