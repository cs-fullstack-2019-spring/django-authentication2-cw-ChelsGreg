# Generated by Django 2.0.6 on 2019-03-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_entry',
            field=models.TextField(max_length=500000000),
        ),
    ]
