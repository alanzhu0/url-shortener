# Generated by Django 3.0.8 on 2020-07-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0002_url_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
