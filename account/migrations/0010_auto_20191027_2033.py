# Generated by Django 2.2.6 on 2019-10-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20191027_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(blank=True, default='tj.png', null=True, upload_to='users/', verbose_name='Аватар'),
        ),
    ]
