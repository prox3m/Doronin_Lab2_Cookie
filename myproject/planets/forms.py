from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label = 'Поиск',
        max_length = 50,
        required = False,

        widget = forms.TextInput(attrs = {
            'placeholder': 'Найти планету...',
            'class': 'search-input',
        }),
    )