# Generated by Django 2.2.6 on 2019-10-24 10:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191024_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='posta',
            name='image',
            field=models.FileField(null=True, upload_to='img/logos/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='posta',
            name='sortutako_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 10, 34, 17, 991310, tzinfo=utc)),
        ),
    ]
