# Generated by Django 3.2 on 2021-08-10 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0017_alter_content_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user_accountant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accountant', to=settings.AUTH_USER_MODEL, verbose_name='Бухгалтер'),
        ),
        migrations.AlterField(
            model_name='application',
            name='user_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to=settings.AUTH_USER_MODEL, verbose_name='Коммерсант'),
        ),
    ]
