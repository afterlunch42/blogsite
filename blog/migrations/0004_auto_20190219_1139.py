# Generated by Django 2.1.7 on 2019-02-19 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190214_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create_time']},
        ),
    ]
