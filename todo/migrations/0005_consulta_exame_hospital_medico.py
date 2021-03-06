# Generated by Django 3.2.9 on 2021-11-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('local', models.CharField(max_length=100, verbose_name='Local')),
                ('diagnosticoMedico', models.TextField(verbose_name='Diagnóstico do Médico')),
                ('requerimentoExame', models.TextField(verbose_name='Requerimento de Exame')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='CRM')),
                ('arquivo', models.CharField(max_length=10000, verbose_name='Nome')),
                ('data', models.DateField(verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Exame',
                'verbose_name_plural': 'Exames',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('endreco', models.CharField(max_length=255, verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Hospital',
                'verbose_name_plural': 'Hospitais',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=20, verbose_name='CRM')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('especialidade', models.TextField(verbose_name='Especialidade do Profissional')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
        ),
    ]
