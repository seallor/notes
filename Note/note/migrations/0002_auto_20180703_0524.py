# Generated by Django 2.0.7 on 2018-07-03 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_title',
            new_name='title',
        ),
    ]
