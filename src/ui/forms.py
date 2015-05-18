from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(label='Query', max_length=100,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control'}))