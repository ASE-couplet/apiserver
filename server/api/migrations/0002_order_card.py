# Generated by Django 2.1.4 on 2018-12-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='card',
            field=models.FileField(null=True, upload_to='card/'),
        ),
    ]