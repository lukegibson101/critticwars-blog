# Generated by Django 3.2.13 on 2022-05-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0005_cwusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
