# Generated by Django 3.2 on 2022-03-24 18:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_advert_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]