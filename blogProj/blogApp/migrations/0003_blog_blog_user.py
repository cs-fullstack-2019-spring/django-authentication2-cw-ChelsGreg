# Generated by Django 2.0.6 on 2019-03-04 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApp', '0002_auto_20190304_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
