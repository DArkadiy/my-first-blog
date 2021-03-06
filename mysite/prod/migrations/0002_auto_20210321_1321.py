# Generated by Django 3.1.7 on 2021-03-21 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prod', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zakaz',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='nom_zak',
            field=models.IntegerField(default='№'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='text',
            field=models.TextField(default='комментарий'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='title',
            field=models.CharField(default='клиент', max_length=200),
        ),
        migrations.CreateModel(
            name='Detal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detal_title', models.CharField(max_length=200)),
                ('detal_size', models.IntegerField()),
                ('detal_weight', models.IntegerField()),
                ('detal_text', models.CharField(default='описание', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('detal_status', models.CharField(max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Деталь',
                'verbose_name_plural': 'Детали',
            },
        ),
    ]
