# Generated by Django 5.0.3 on 2024-05-05 17:28

import apps.personal.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_profissionalexperienceitem_years'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('bi', models.FileField(upload_to=apps.personal.models.function_upload_to)),
                ('cv', models.FileField(upload_to=apps.personal.models.function_upload_to)),
                ('certificate_literary', models.FileField(upload_to=apps.personal.models.function_upload_to)),
                ('medical_certificate', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc1', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc2', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc3', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc4', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc5', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc6', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc7', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc8', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc9', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('other_doc10', models.FileField(blank=True, null=True, upload_to=apps.personal.models.function_upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Documentos',
                'ordering': ['user', '-created_at'],
            },
        ),
    ]