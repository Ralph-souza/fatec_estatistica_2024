from django import forms


class CalculationForm(forms.Form):
    value_a = forms.FloatField(label='Valor A')
    value_b = forms.FloatField(label='Valor B')
    value_c = forms.FloatField(label='Valor C', required=False)
    value_d = forms.FloatField(label='Valor D', required=False)
