# Generated by Django 3.2 on 2022-04-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_advert_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]