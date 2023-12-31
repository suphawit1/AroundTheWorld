# Generated by Django 4.2.5 on 2023-09-23 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('AccomName', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('TypeRoom', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Countrys',
            fields=[
                ('CountryName', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Region', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('LocationName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('CountryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tours.countrys')),
            ],
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('TourName', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Status', models.TextField(choices=[('เปิด', 'เปิด'), ('ปิด', 'ปิด'), ('เต็ม', 'เต็ม')], default='open')),
                ('TripDuration', models.TextField()),
                ('Day', models.DateField()),
                ('price', models.FloatField(default=0)),
                ('FlightNo', models.IntegerField()),
                ('Accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tours.accommodation')),
                ('CountryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tours.countrys')),
                ('GuideName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employee.guidetour')),
                ('ListLoID', models.ManyToManyField(to='app_tours.locations')),
            ],
        ),
        migrations.AddField(
            model_name='accommodation',
            name='CountryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tours.countrys'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='LocationName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tours.locations'),
        ),
    ]
