# Generated by Django 4.2.4 on 2023-09-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tours', '0003_alter_detailtour_tour_alter_detailtour_immage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtour',
            name='Detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
