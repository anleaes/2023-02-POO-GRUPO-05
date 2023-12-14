# Generated by Django 4.1 on 2023-12-13 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('veiculos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('gerente', models.CharField(max_length=50, verbose_name='Gerente')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.veiculo')),
            ],
            options={
                'verbose_name': 'Loja',
                'verbose_name_plural': 'Lojas',
                'ordering': ['id'],
            },
        ),
    ]
