# Generated by Django 2.2 on 2019-05-07 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190506_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.TaskList'),
        ),
    ]
