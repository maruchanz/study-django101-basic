# Generated by Django 3.1.7 on 2021-03-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spicy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='character_features',
            field=models.TextField(max_length=30, null=True, verbose_name='特徴'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='character_name',
            field=models.TextField(max_length=30, null=True, verbose_name='名前'),
        ),
    ]
