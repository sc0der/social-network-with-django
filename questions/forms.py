from django import forms
from .models import Savolho
from django.db.transaction import commit

class SavolForm(forms.ModelForm):
    class Meta:
        model = Savolho
        fields = (
            'title', 'image', 'savol', 'subject'
        )
        widget = {
            "title": forms.TextInput(attrs={'placeholder': 'Заголовка вопроса'}),
            "image": forms.ImageField(),
            "savol": forms.Textarea(attrs={'placeholder': 'Заголовка вопроса'}),
            "subject": forms.SelectMultiple(attrs={'placeholder': 'Заголовка вопроса'}),
        }

class SavolEditForm(forms.ModelForm):
    class Meta:
        model = Savolho
        fields = ('title', 'image', "savol")