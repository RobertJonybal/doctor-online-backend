# Generated by Django 2.1.1 on 2018-09-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='number',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
