from django import forms


class SentenceForm(forms.Form):
    sentence = forms.CharField(label='Sentence', max_length=100)