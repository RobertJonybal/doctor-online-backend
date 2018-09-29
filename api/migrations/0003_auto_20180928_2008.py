# Generated by Django 2.1.1 on 2018-09-28 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180928_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduel',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_schedule', to=settings.AUTH_USER_MODEL),
        ),
    ]
