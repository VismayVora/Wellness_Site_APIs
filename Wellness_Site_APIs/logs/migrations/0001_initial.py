# Generated by Django 3.2.8 on 2021-10-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('food_type', models.CharField(choices=[('S', 'Solid'), ('L', 'Liquid')], default='S', max_length=2)),
                ('quantity', models.IntegerField()),
                ('consumption_time', models.DateTimeField(blank=True, null=True)),
                ('calories', models.DecimalField(decimal_places=3, max_digits=6)),
                ('notes', models.TextField(max_length=300)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
