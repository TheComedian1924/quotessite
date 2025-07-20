from .models import Quotedatabase
from django.forms import ModelForm, Textarea, TextInput, NumberInput


class QuotesdatabaseForm(ModelForm):
    class Meta:
        model = Quotedatabase
        fields = ['text', 'source', 'weight']
        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст цитаты'
            }),
            "source": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Источник цитаты'
            }),
            "weight": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес цитаты'
            })
        }