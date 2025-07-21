from django.core.exceptions import ValidationError
from .models import Quotes
from django.forms import ModelForm, Textarea, TextInput, NumberInput


class QuotesForm(ModelForm):
    class Meta:
        model = Quotes
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
                'placeholder': 'Вес цитаты (от 1 до 10)'
            })
        }
    def clean_source(self):
        sourcecheck = self.cleaned_data['source']
        count = Quotes.objects.filter(source=sourcecheck).count()
        if 'http://' in sourcecheck or 'https://' in sourcecheck or 'www.' in sourcecheck:
            raise ValidationError('Ссылки запрещены в цитате.')
        if count >= 3:
            raise ValidationError('Нельзя добавить больше 3 цитат от одного источника.')
        return sourcecheck

    def clean_text(self):
        textcheck = self.cleaned_data['text']
        if 'http://' in textcheck or 'https://' in textcheck or 'www.' in textcheck:
            raise ValidationError('Ссылки запрещены в цитате.')
        return textcheck