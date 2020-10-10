# Generated by Django 3.1.2 on 2020-10-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20201010_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='editor',
            new_name='image_author',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='location/'),
        ),
    ]