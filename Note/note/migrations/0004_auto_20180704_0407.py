# Generated by Django 2.0.7 on 2018-07-04 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_unique_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='unique_words',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]