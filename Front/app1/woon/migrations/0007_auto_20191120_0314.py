# Generated by Django 2.1.7 on 2019-11-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woon', '0006_auto_20191120_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='photos/images/'),
        ),
    ]