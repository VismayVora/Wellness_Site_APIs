# Generated by Django 3.2.8 on 2021-10-16 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietlog',
            name='notes',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='WorkoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('workout_time', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=300, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WorkoutLog', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]