# Generated by Django 3.2.12 on 2022-03-29 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_webpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('code', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='code',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.contestant'),
        ),
    ]
