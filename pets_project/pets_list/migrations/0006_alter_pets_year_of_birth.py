# Generated by Django 4.2 on 2024-11-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_list', '0005_alter_breeds_options_alter_pets_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='year_of_birth',
            field=models.DateField(default=None, null=True),
        ),
    ]
