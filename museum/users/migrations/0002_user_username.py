# Generated by Django 4.1.6 on 2023-02-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='somename', help_text='127 symbols max', max_length=127, verbose_name='username'),
        ),
    ]
