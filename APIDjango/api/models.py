from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Sexo(models.Model):
    idSexo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre
    
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    idUsuario = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    password = models.CharField(max_length=128)
    especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE, null=True)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, null=True)

    github_username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    github_access_token = models.CharField(max_length=255, blank=True, null=True)

    register_date = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='alumno_user_groups',  
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='alumno_user_permissions',
        blank=True,
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_de_nacimiento', 'especialidad', 'sexo']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

class Profile(models.Model):
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)