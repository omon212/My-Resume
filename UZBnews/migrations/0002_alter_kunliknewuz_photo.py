# Generated by Django 4.2.5 on 2023-09-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UZBnews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kunliknewuz',
            name='photo',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]