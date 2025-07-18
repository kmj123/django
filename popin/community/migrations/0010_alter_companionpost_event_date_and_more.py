# Generated by Django 5.2.1 on 2025-07-09 04:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_alter_companionpost_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companionpost',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='행사 날짜 및 시간'),
        ),
        migrations.AlterField(
            model_name='companionpost',
            name='max_people',
            field=models.PositiveIntegerField(default=1, verbose_name='최대 모집 인원'),
        ),
        migrations.AlterField(
            model_name='proxypost',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='이벤트 날짜 및 시간'),
        ),
        migrations.AlterField(
            model_name='proxypost',
            name='max_people',
            field=models.PositiveIntegerField(default=1, verbose_name='최대 모집 인원'),
        ),
    ]
