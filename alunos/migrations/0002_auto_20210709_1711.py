# Generated by Django 3.1.5 on 2021-07-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
