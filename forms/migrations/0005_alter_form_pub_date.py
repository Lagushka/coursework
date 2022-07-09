# Generated by Django 4.0.5 on 2022-07-07 14:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_alter_form_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 14, 21, 45, 556814, tzinfo=utc), verbose_name='date published'),
        ),
    ]
