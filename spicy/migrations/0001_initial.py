# Generated by Django 3.1.7 on 2021-03-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_data', models.CharField(choices=[('M', '男性'), ('W', '女性'), ('N', 'その他')], max_length=4, verbose_name='性別')),
                ('character_name', models.CharField(max_length=30, verbose_name='特徴')),
            ],
        ),
    ]