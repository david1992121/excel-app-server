# Generated by Django 3.2.7 on 2021-09-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='order',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='順序'),
        ),
    ]
