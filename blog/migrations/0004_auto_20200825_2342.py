# Generated by Django 3.1 on 2020-08-25 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200825_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name=''),
        ),
    ]
