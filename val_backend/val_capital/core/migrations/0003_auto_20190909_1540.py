# Generated by Django 2.2 on 2019-09-09 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190909_1527'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deposit',
            new_name='Commitment',
        ),
        migrations.RenameField(
            model_name='drawdown',
            old_name='deposit',
            new_name='commitment',
        ),
    ]