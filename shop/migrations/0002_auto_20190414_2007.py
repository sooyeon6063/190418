# Generated by Django 2.1.5 on 2019-04-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
