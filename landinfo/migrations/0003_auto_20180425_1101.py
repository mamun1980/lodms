# Generated by Django 2.0.2 on 2018-04-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landinfo', '0002_auto_20180425_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plotmeta',
            old_name='total_bondobosto_land',
            new_name='alluvion_diluvion',
        ),
        migrations.RenameField(
            model_name='plotmeta',
            old_name='total_khas_land',
            new_name='non_settleable_land',
        ),
        migrations.RenameField(
            model_name='plotmeta',
            old_name='total_orpito_land',
            new_name='settleable_land',
        ),
        migrations.RenameField(
            model_name='plotmeta',
            old_name='total_recorded_land',
            new_name='surrendered_land',
        ),
        migrations.AlterField(
            model_name='plotmeta',
            name='total_amount_of_land',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
    ]
