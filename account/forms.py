from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Person
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
# Person = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model = Person
        fields = ('username', 'password')
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('username', 'f_name',
            'l_name','birth_date',
            'email',
            'city', 'gen', 'person',
            'unis', 'avatar'
            )
    
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Рамз', widget=forms.PasswordInput)
    class Meta:
        model = Person
        fields = ('username', 'f_name',
            'l_name','birth_date',
            'email','avatar',
            'city', 'person',
            'unis', 'gen'
        ) 
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = Person.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Чунин ном алакай вуҷуд дорад")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        sd = Person.objects.filter(email = email)
        if sd.exists():
            raise forms.ValidationError("Инхел email вуҷуд дорад")
        return email