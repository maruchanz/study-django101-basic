from django import forms 
from spicy.models import questionnaire
from django.contrib.auth.forms import (
    AuthenticationForm
)

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = questionnaire
        fields = ('character_name', 'gender_data', 'character_features','media_data','URL')

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
