# Generated by Django 3.2.12 on 2022-03-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20220329_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestant',
            name='code',
        ),
    ]