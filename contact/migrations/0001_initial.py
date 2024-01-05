# Generated by Django 5.0.1 on 2024-01-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('send_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]