# Generated by Django 3.0.3 on 2020-02-26 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messager',
            new_name='message',
        ),
    ]
