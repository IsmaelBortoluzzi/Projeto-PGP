# Generated by Django 4.1 on 2023-04-27 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demanda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContasPagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=16)),
                ('demanda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demanda.demanda')),
            ],
        ),
    ]
