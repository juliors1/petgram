# Generated by Django 3.1.6 on 2021-02-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210210_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]