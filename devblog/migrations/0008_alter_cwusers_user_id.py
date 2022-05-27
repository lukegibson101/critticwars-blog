# Generated by Django 3.2.13 on 2022-05-27 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devblog', '0007_alter_comment_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cwusers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cw_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
