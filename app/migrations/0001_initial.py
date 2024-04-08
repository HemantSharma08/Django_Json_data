# Generated by Django 5.0.4 on 2024-04-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('insight', models.TextField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
