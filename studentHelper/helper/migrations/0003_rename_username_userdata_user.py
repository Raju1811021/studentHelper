# Generated by Django 3.2.13 on 2022-05-06 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20220506_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='username',
            new_name='user',
        ),
    ]
