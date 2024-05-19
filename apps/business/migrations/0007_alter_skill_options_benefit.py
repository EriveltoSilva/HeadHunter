# Generated by Django 5.0.3 on 2024-05-16 12:07

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_rename_address_vacancy_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['title', '-created_at'], 'verbose_name_plural': 'Habilidades Requeridas'},
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.vacancy')),
            ],
            options={
                'verbose_name_plural': 'Beneficios de Trabalho',
                'ordering': ['title', '-created_at'],
            },
        ),
    ]