# Generated by Django 3.1.5 on 2021-07-09 20:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_auto_20210709_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF'),
        ),
    ]
