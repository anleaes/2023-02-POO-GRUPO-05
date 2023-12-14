# Generated by Django 4.1 on 2023-12-13 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formapagamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=50)),
                ('km', models.FloatField()),
                ('categoria', models.CharField(max_length=50)),
                ('forma_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formapagamento.formapagamento')),
            ],
        ),
    ]