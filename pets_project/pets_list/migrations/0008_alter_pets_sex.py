# Generated by Django 5.1.3 on 2024-11-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_list', '0007_alter_pets_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='sex',
            field=models.BooleanField(null=True),
        ),
    ]
