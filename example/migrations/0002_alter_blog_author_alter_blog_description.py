# Generated by Django 4.1.3 on 2022-12-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("example", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
