# Generated by Django 2.0.6 on 2019-03-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_entry', models.TextField(max_length='')),
            ],
        ),
    ]
