# Generated by Django 3.2.12 on 2022-03-19 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0017_auto_20220319_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='workperformed',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Count'),
        ),
        migrations.AddField(
            model_name='workperformed',
            name='uom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.unitsofmeasurement'),
        ),
    ]
