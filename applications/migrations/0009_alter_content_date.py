# Generated by Django 3.2 on 2021-08-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0008_content_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date',
            field=models.TimeField(null=True, verbose_name='Сроки'),
        ),
    ]
