# Generated by Django 4.1.1 on 2022-10-30 11:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pursuit_app', '0007_alter_img_member_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='assignee',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
