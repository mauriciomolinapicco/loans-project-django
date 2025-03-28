from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import LoanApplication
from .forms import LoanApplicationForm
from django.urls import reverse
import uuid

"""
    para correr estos tests unitarios simplemente:
        python manage.py test
"""

class LoanApplicationModelTest(TestCase):

    def test_instance_creation(self):
        """
        test unitario de la creacion de una instancia
        """
        application = LoanApplication.objects.create(
            dni='12345678',
            cuil='20221234567',
            first_name='Leo',
            last_name='Messi',
            email='messi@example.com',
            gender='Masculino',
            amount=101010.0
        )

        self.assertEqual(application.first_name, 'Leo')
        self.assertEqual(application.last_name, 'Messi')
        self.assertEqual(application.amount, 101010.0)
        self.assertTrue(application.id)



class LoanApplicationFormTestCase(TestCase):
    """
        test del ModelForm definido en forms.py
    """
    def test_valid_form(self):
        data = {
            'dni': '12345678',
            'cuil': '20221234567',
            'first_name': 'Carlos',
            'last_name': 'Méndez',
            'email': 'carlos@example.com',
            'gender': 'Masculino',
            'amount': 1000.0,
        }
        form = LoanApplicationForm(data)
        self.assertTrue(form.is_valid())  

    def test_invalid_form(self):
        data = {
            'dni': '',  # DNI vacío debería ser inválido
            'cuil': '20221234567',
            'first_name': 'Sara',
            'last_name': 'Gómez',
            'email': 'sara@example.com',
            'gender': 'Femenino',
            'amount': 2000.0,
        }
        form = LoanApplicationForm(data)
        self.assertFalse(form.is_valid())  
        self.assertIn('dni', form.errors) 



class TestApplicationDetailView(TestCase):
    """
        Test de la vista de detalle de una aplicacion
    """
    def test_application_detail_found(self):
        loan_application = LoanApplication.objects.create(
            dni="12345678",
            cuil="20-12345678-9",
            first_name="Cuti",
            last_name="Romero",
            email="cuti@gmail.com",
            gender="Masculino",
            amount=1000
        )
        response = self.client.get(reverse('application_detail', args=[loan_application.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cuti Romero") 