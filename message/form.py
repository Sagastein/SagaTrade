
from django import forms

from .models import ConversationMessage


class ConversationForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
            'class': 'w-full  rounded-xl',
            })
        }
