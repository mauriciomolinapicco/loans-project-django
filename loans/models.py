from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import uuid

GENDER_CHOICES = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
)

dni_validator = RegexValidator(r'^\d{7,8}$', "El DNI debe ser un entero entre 7 y 8 caracteres")
cuil_validator = RegexValidator(r'^\d{10,11}$', "El CUIL debe ser un entero entre 10 y 11 caracteres")
name_validator = RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', 'El nombre y apellido solo pueden contener letras y espacios.')


class User(AbstractUser):
    pass
    """
    la clase usuario hereda de la clase abstracta AbstractUser y para este caso no necesito agregar ningun atributo
    """


class LoanApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """
       Elegi usar UUIDs en lugar de id secuencial porque ayuda a mejorar la seguridad, 
        ya que hace más difícil adivinar o predecir los IDs de los registros. Esto es especialmente 
        útil para evitar ataques donde un atacante podría intentar adivinar o enumerar los registros 
        a través de URLs o patrones en la base de datos.
    """
    dni = models.CharField(max_length=8, validators=[dni_validator])
    cuil = models.CharField(max_length=11, validators=[cuil_validator])
    first_name = models.CharField(max_length=255, validators=[name_validator])
    last_name = models.CharField(max_length=255, validators=[name_validator])
    email = models.EmailField(error_messages={
                'invalid': 'Por favor, ingrese un correo electrónico válido.'
            })
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES)
    amount = models.DecimalField(max_digits=8, decimal_places=1, 
            error_messages={
                'invalid': 'El monto debe ser un número con un máximo de 7 dígitos y 1 decimal.'
            })
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True) #se define automaticamente cuando se crea la instancia

    def __str__(self):
        return f"Prestamo de {self.first_name} {self.last_name} por ${self.amount}"
    
    def __repr__(self):
        return f"Prestamo de {self.first_name} {self.last_name} ({self.gender}) por ${self.amount} el {self.created_date}"
