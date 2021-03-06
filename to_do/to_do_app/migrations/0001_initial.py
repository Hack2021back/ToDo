# Generated by Django 3.2.9 on 2021-12-04 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('end_data', models.DateField(blank=True)),
                ('start_data', models.DateField()),
                ('time', models.TimeField()),
                ('priority', models.CharField(choices=[('1', 'priority1'), ('2', 'priority2'), ('3', 'priority3'), ('4', 'priority4')], max_length=10)),
            ],
            options={
                'verbose_name': 'Plans',
                'verbose_name_plural': 'Plans',
                'ordering': ['priority', 'task'],
            },
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.ManyToManyField(blank=True, related_name='tasks_of_user', to='to_do_app.ToDoList')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
