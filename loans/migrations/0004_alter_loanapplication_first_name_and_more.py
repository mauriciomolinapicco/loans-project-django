# Generated by Django 5.0.6 on 2025-03-28 12:21

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_rename_timestamp_loanapplication_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='first_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', 'El nombre y apellido solo pueden contener letras y espacios.')]),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='last_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', 'El nombre y apellido solo pueden contener letras y espacios.')]),
        ),
    ]
