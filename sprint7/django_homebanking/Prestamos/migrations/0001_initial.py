# Generated by Django 4.1 on 2022-08-13 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=11)),
                ('loan_date', models.CharField(max_length=10)),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente')),
            ],
        ),
    ]