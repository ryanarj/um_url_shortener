# Generated by Django 4.1.1 on 2022-10-01 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pregenerate_url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregenerateurl',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregenerateurl',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
