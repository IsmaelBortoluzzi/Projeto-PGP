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
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processo', models.CharField(default='', max_length=16)),
                ('status', models.CharField(default='', max_length=16)),
                ('demanda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demanda.demanda')),
            ],
        ),
    ]
