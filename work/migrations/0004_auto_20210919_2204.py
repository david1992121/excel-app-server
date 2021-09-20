# Generated by Django 3.2.7 on 2021-09-19 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20210919_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratio',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratio',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
        migrations.AddField(
            model_name='sheet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
