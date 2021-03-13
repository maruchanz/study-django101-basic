from django.db import models
# import spicy.choice
# Create your models here.


GENDER_CHOICE = (
        ('M','男性'),
        ('W','女性'),
        ('N','その他'),
    )


class questionnaire(models.Model):
    # class Meta:
    #     db_table = 'questionnaire' 
    character_name = models.CharField(verbose_name="名前",null =False, max_length = 30)    
    gender_data = models.CharField(verbose_name="性別", choices = GENDER_CHOICE, max_length = 4)
    character_features = models.CharField(verbose_name="特徴", null = False ,max_length = 30)    
    media_data = models.ImageField(verbose_name ="画像", blank = False, null = True, upload_to = 'media/maimages')

    def __str__(self):
        return self.character_name

