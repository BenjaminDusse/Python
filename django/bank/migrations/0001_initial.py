# Generated by Django 3.2.13 on 2022-06-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('row1', models.CharField(blank=True, max_length=50, null=True)),
                ('row2', models.CharField(blank=True, max_length=50, null=True)),
                ('row3', models.CharField(blank=True, max_length=50, null=True)),
                ('row4', models.CharField(blank=True, max_length=50, null=True)),
                ('row5', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
