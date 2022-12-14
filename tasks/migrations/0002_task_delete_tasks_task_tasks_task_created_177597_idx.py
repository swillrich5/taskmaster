# Generated by Django 4.1.1 on 2022-11-18 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('UN', 'Unassigned'), ('IP', 'In Progress'), ('CL', 'Closed')], default='UN', max_length=2)),
                ('priority', models.CharField(choices=[('HI', 'High'), ('MD', 'Medium'), ('LO', 'Low')], default='LO', max_length=2)),
                ('assigned_to', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['-created'], name='tasks_task_created_177597_idx'),
        ),
    ]
