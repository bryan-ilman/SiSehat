# Generated by Django 4.1 on 2022-10-28 10:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrasi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokter',
            name='nomor_induk_kependudukan',
            field=models.CharField(max_length=24, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{16}$')]),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='nomor_induk_kependudukan',
            field=models.CharField(max_length=24, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{16}$')]),
        ),
    ]
