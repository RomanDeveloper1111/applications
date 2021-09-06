# Generated by Django 3.2 on 2021-08-02 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('text_number', models.CharField(max_length=20, verbose_name='Порядковый номер')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('note', models.TextField(max_length=250, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Содержимое заявки',
            },
        ),
        migrations.CreateModel(
            name='TypeOfApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Тип заявки')),
            ],
            options={
                'verbose_name': 'Тип заявки',
                'verbose_name_plural': 'Типы заявок',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('note_mistake', models.TextField(max_length=250, verbose_name='Замечание')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.content', verbose_name='Содержимое')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='applications.typeofapp', verbose_name='Тип заявки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
