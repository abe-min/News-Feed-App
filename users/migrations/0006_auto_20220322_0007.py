# Generated by Django 3.2.6 on 2022-03-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220321_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='staff',
            new_name='Business',
        ),
        migrations.AddField(
            model_name='profile',
            name='Entertainment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='General',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Health',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Science',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Sports',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Technology',
            field=models.BooleanField(default=False),
        ),
    ]
