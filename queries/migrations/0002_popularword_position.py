# Generated by Django 2.2.14 on 2020-07-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularword',
            name='position',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
