# Generated by Django 3.2.12 on 2022-03-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_auto_20220316_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='start_work',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='start_work'),
        ),
        migrations.AlterField(
            model_name='workperformed',
            name='finish_work',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='finish_work'),
        ),
        migrations.AlterField(
            model_name='workperformed',
            name='start_work',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='start_work'),
        ),
    ]
