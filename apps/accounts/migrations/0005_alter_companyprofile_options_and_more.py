# Generated by Django 5.0.3 on 2024-05-16 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_companyprofile_facebook_companyprofile_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyprofile',
            options={'ordering': ['user'], 'verbose_name_plural': 'Perfis Empresariais'},
        ),
        migrations.AlterModelOptions(
            name='personalprofile',
            options={'ordering': ['user'], 'verbose_name_plural': 'Perfis de Usuários'},
        ),
    ]