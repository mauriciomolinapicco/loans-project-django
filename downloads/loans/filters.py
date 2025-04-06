import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import LoanApplication

class LoanApplicationFilter(django_filters.FilterSet):
    """
    Filtro para el modelo `LoanApplication`, que permite filtrar las aplicaciones de préstamo
    según varios criterios, tales como fecha de creación, nombre, apellido y monto.

    La clase `LoanApplicationFilter` proporciona una interfaz para aplicar múltiples filtros en los registros de préstamos.

    La clase `Meta` configura el modelo y los campos a los que se les aplicarán los filtros:
        - Se filtran todos los campos del modelo `LoanApplication` excepto `email`, `created_date`, `first_name`, `last_name`, `amount`, y `gender`.
    """

    start_date = DateFilter(field_name="created_date", lookup_expr='gte', label='Fecha desde (mm/dd/yyyy)')
    end_date = DateFilter(field_name="created_date", lookup_expr='lte',label='Fecha hasta (mm/dd/yyyy)')
    name_filter = CharFilter(field_name='first_name', lookup_expr='icontains',label='El nombre contiene: ')
    last_name_filter = CharFilter(field_name='last_name', lookup_expr='icontains',label='El apellido contiene: ')
    amount_filter = NumberFilter(field_name='amount',lookup_expr='gte', label='Monto mayor a:')

    class Meta:
        model = LoanApplication
        fields = '__all__'
        exclude = ['email', 'created_date', 'first_name', 'last_name', 'amount','gender', 'id']