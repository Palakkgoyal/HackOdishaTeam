# Generated by Django 4.2.5 on 2023-09-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planttree',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
