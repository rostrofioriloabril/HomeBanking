# Generated by Django 4.0.6 on 2022-08-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProceso', '0003_remove_sucursal_branch_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('branch_id', models.IntegerField()),
            ],
        ),
    ]