# Generated by Django 3.2.13 on 2022-07-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('robot_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('pet', models.BooleanField()),
                ('city', models.CharField(max_length=200)),
                ('hair_color', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
