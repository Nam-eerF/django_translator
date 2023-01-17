from django import forms
from googletrans import LANGCODES

LANGUAGES_FROM = ((code, lang) for lang, code in LANGCODES.items())
LANGUAGES_TO = ((code, lang) for lang, code in LANGCODES.items())


class TranslateForm(forms.Form):
    lang_from = forms.ChoiceField(choices=LANGUAGES_FROM, widget=forms.Select(attrs={'class': 'form-select'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    lang_to = forms.ChoiceField(choices=LANGUAGES_TO, widget=forms.Select(attrs={'class': 'form-select'}))
