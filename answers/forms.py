from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField()
    class Meta:
        model = Comment
        fields = ('text',)