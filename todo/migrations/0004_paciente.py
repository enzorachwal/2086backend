# Generated by Django 3.1.5 on 2021-10-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_comorbidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('condicoesMedicas', models.TextField(verbose_name='Condições Médicas')),
                ('comorbidades', models.ManyToManyField(to='todo.Comorbidade', verbose_name='Comorbidades')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
