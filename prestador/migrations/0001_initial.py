# Generated by Django 4.1 on 2023-04-27 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12)),
                ('documento', models.CharField(max_length=14, unique=True)),
                ('chave_pix', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('comissao', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]