# Generated by Django 2.2.6 on 2019-10-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191024_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posta',
            name='sortutako_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
