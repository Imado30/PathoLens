# Generated by Django 5.1.3 on 2024-12-12 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0008_alter_diagnosis_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usetime',
            name='action',
        ),
        migrations.RemoveField(
            model_name='usetime',
            name='timeID',
        ),
        migrations.RemoveField(
            model_name='usetime',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='usetime',
            name='actionTime',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='usetime',
            name='diagID',
            field=models.ForeignKey(db_column='diagID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='image.diagnosis'),
        ),
    ]
