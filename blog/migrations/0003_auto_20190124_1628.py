# Generated by Django 2.1.5 on 2019-01-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190124_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.IntegerField(choices=[(2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022')], default=2019, max_length=4),
        ),
    ]
