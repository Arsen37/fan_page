# Generated by Django 3.2.8 on 2021-11-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20211109_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentaries',
            name='commentary',
            field=models.TextField(verbose_name='What you think?'),
        ),
    ]
