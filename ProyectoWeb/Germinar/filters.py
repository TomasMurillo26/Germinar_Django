from dataclasses import Field
import django_filters
from .models import producto, catProducto


class FiltroVista(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascendente'),
        ('descending', 'Descendente')
    )

    ordering = django_filters.ChoiceFilter(label='Ordenar por precio', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = producto
        fields = {
			'categoria' : ['exact'],
			'precio':['lt','gt'],
        }


    def filter_by_order(self, queryset, name, value):
        expression = 'precio' if value == 'ascending' else '-precio'
        return queryset.order_by(expression)


    def __init__(self, *args, **kwargs):
        super(FiltroVista, self).__init__(*args, **kwargs)
        categoria_defecto = catProducto.objects.get(idCategoria = 1)
        self.form.initial['categoria'] = categoria_defecto
