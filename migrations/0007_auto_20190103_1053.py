# Generated by Django 2.1.2 on 2019-01-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20190101_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pcs',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='picss',
            field=models.ImageField(upload_to='media/'),
        ),
    ]