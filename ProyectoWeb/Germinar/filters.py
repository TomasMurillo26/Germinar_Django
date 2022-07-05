import django_filters
from .models import producto

class FiltroVista(django_filters.FilterSet):

	CHOICES = (
        ('ascending', 'Ascendente'),
        ('descending', 'Descendente')
    )

    ordering = django_filters.ChoiceFilter(label='Ordenar por precio', choices=CHOICES, method='filter_by_order')

	class Meta:
		model = producto
		fields = {
			'nombre' : ['icontains'],
			'categoria' : ['icontains'],
			'precio':['lt','gt'],
		}

    def filter_by_order(self, queryset, name, value):
        expression = 'precio' if value == 'ascending' else '-precio'
        return queryset.order_by(expression)