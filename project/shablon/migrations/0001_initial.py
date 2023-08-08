# Generated by Django 4.2.4 on 2023-08-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_st', models.CharField(max_length=300, unique=True)),
                ('text_st', models.TextField()),
                ('data_cr_st', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
