from django.db import models

# Create your models here.

GENDER_CHOICE = (
    ('M','男性'),
    ('W','女性'),
    ('N','その他'),
)

class questionnaire(models.Model):
    character_name = models.TextField(verbose_name="名前",null =True, max_length = 30)    
    gender_data = models.CharField(verbose_name="性別", choices = GENDER_CHOICE, max_length = 4)
    character_features = models.TextField(verbose_name="特徴", null = True,max_length = 30)    

