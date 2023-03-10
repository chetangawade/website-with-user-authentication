# Generated by Django 4.0.3 on 2022-05-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=17)),
                ('last_name', models.CharField(max_length=17)),
                ('user_name', models.CharField(max_length=17)),
                ('email', models.EmailField(max_length=17)),
                ('mobile', models.CharField(max_length=17)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
