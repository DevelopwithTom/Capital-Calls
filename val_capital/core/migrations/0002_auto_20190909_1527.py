# Generated by Django 2.2 on 2019-09-09 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commitment',
            new_name='Drawdown',
        ),
        migrations.AlterModelOptions(
            name='deposit',
            options={'ordering': ['date']},
        ),
    ]
