# Generated by Django 2.2.6 on 2019-10-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191027_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person',
            field=models.IntegerField(choices=[('student', 'Студент'), ('teacher', 'Предодаватель')], verbose_name='кто Вы'),
        ),
    ]
