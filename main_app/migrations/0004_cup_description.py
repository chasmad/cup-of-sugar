# Generated by Django 3.0.2 on 2020-03-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200323_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='cup',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
