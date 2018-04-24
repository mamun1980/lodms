# Generated by Django 2.0.2 on 2018-04-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landinfo', '0005_auto_20180424_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mouza',
            options={'verbose_name': 'Mouza', 'verbose_name_plural': 'Mouzas'},
        ),
        migrations.AlterModelOptions(
            name='plot',
            options={'verbose_name': 'Plot', 'verbose_name_plural': 'Plots'},
        ),
        migrations.AlterField(
            model_name='mouzameta',
            name='total_khas_land',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
    ]