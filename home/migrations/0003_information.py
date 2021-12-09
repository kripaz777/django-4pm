# Generated by Django 3.2.9 on 2021-12-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_address', models.TextField()),
                ('per_address', models.TextField()),
                ('phone', models.CharField(max_length=500)),
                ('timing', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]