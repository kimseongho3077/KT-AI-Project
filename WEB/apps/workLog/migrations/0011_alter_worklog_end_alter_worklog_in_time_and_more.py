# Generated by Django 4.2 on 2023-06-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workLog", "0010_worklog_approved_worklog_region"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worklog",
            name="end",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="in_time",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="out_time",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="start",
            field=models.DateField(),
        ),
    ]
