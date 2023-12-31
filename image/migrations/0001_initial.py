# Generated by Django 4.2.6 on 2023-10-27 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('colour', models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('white', 'white'), ('black', 'black')], default='red', max_length=20)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create date')),
            ],
        ),
    ]
