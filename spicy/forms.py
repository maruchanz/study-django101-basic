from django import forms 
from spicy.models import questionnaire


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = questionnaire
        fields = ('character_name', 'gender_data', 'character_features')