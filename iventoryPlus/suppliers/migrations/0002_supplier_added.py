# Generated by Django 4.2.13 on 2024-07-28 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplier",
            name="added",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
