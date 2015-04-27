from django import forms


class SentenceForm(forms.Form):
    sentence = forms.CharField(label='Sentence', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))