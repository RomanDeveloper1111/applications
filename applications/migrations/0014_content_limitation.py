# Generated by Django 3.2 on 2021-08-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0013_remove_content_limitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='limitation',
            field=models.DateField(null=True, verbose_name='Сроки'),
        ),
    ]
