# Generated by Django 2.0.9 on 2018-11-24 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20181125_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]