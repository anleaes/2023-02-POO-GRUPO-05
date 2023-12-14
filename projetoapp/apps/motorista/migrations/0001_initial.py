# Generated by Django 4.1 on 2023-12-13 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carteira', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('carteira', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carteira.carteira')),
            ],
            options={
                'verbose_name': 'Motorista',
                'verbose_name_plural': 'Motoristas',
                'ordering': ['id'],
            },
        ),
    ]
