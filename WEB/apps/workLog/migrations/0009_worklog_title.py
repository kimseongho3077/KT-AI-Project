# Generated by Django 4.2 on 2023-06-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workLog", "0008_alter_worklog_contents_alter_worklog_day_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="worklog",
            name="title",
            field=models.CharField(default="작업 승인 요청", max_length=50),
        ),
    ]
