# Generated by Django 3.0.6 on 2020-07-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yektaneturl',
            name='shortcode',
            field=models.CharField(default='YektanetDefaultValue', max_length=15),
            preserve_default=False,
        ),
    ]
