# Generated by Django 4.0 on 2024-02-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlines', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
