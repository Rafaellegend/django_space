# Generated by Django 5.0.7 on 2024-09-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
