# Generated by Django 4.2.5 on 2023-10-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tours', '0006_alter_tours_immage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='immage',
            field=models.ImageField(null=True, upload_to='static/app_tour/'),
        ),
    ]
