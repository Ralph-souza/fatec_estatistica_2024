import math

from django.shortcuts import render

from .forms import CalculationForm


def get_average(value_a, value_b):
    return (value_a + value_b) / 2


def get_variancy(value_a, value_b):
    return ((value_b - value_a) ** 2) / 12


def standard_deviation(value_a, value_b):
    return math.sqrt(get_variancy(value_a, value_b))


def coefficient_variation(value_a, value_b):
    return (100 * standard_deviation(value_a, value_b)) / get_average(value_a, value_b)


def calculate(request):
    result = {
        'average': None,
        'variancy': None,
        'standard_deviantion': None,
        'coefficient_variation': None,
        'probability': None

    }

    form = CalculationForm(request.POST or None)

    if form.is_valid():
        value_a = form.cleaned_data['value_a']
        value_b = form.cleaned_data['value_b']
        value_c = form.cleaned_data['value_c']
        value_d = form.cleaned_data['value_d']

        result['average'] = f"{get_average(value_a, value_b):.2f}"
        result['variancy'] = f"{get_variancy(value_a, value_b):.4f}"
        result['standard_deviation'] = f"{standard_deviation(value_a, value_b):.4f}"
        result['coefficient_variation'] = f"{coefficient_variation(value_a, value_b):.2f}%"

        if value_c is not None and value_d is not None:
            pass

            result['probability'] = f'Probabilidade de C={value_c} e D={value_d}'

    return render(request, 'calculate.html', {'form': form, 'result': result})
