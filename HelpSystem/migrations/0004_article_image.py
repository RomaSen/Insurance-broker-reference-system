# Generated by Django 3.0.2 on 2020-03-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpSystem', '0003_auto_20200320_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='articles/', verbose_name='Изображение'),
        ),
    ]
