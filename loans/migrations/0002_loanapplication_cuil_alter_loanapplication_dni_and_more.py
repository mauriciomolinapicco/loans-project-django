# Generated by Django 5.0.6 on 2025-03-27 23:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='cuil',
            field=models.CharField(default=11111111111, max_length=11, validators=[django.core.validators.RegexValidator('^\\d{10,11}$', 'El CUIL debe ser un entero entre 10 y 11 caracteres')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='dni',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\d{7,8}$', 'El DNI debe ser un entero entre 7 y 8 caracteres')]),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='first_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', 'El nombre y apellido solo pueden contener letras, espacios y guiones.')]),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='last_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$', 'El nombre y apellido solo pueden contener letras, espacios y guiones.')]),
        ),
    ]
