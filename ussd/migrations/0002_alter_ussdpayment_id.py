# Generated by Django 4.0.3 on 2022-04-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ussdpayment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
