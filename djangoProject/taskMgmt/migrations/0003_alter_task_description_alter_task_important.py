# Generated by Django 4.0.2 on 2024-05-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskMgmt', '0002_task_description_task_due_date_task_due_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]