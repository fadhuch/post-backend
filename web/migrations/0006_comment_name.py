# Generated by Django 3.2.5 on 2021-07-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
