# Generated by Django 3.2.13 on 2022-05-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0003_blog_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]
