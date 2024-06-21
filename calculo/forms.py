from django import forms


class CalculationForm(forms.Form):
    value_a = forms.FloatField(label='Valor A', required=True)
    value_b = forms.FloatField(label='Valor B', required=True)
    value_c = forms.FloatField(label='Valor C', required=False)
    value_d = forms.FloatField(label='Valor D', required=False)

    def clean(self):
        cleaned_data = super().clean()
        value_a = cleaned_data.get('value_a')
        value_b = cleaned_data.get('value_b')
        value_c = cleaned_data.get('value_c')
        value_d = cleaned_data.get('value_d')

        if value_a is not None and value_b is not None and value_a > value_b:
            self.add_error('value_a', 'Valor A deve ser menor ou igual a Valor B.')
            self.add_error('value_b', 'Valor B deve ser maior ou igual a Valor A.')
        
        if value_c is not None and value_d is not None and value_c > value_d:
            self.add_error('value_c', 'Valor C deve ser menor ou igual a Valor D.')
            self.add_error('value_d', 'Valor D deve ser maior ou igual a Valor C.')
        
        return cleaned_data