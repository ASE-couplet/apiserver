# Generated by Django 2.2.dev20181219114131 on 2018-12-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('tags', models.TextField(null=True)),
                ('poem', models.TextField(null=True)),
            ],
        ),
    ]
