# Generated by Django 4.1.7 on 2023-03-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category_sector_description', models.TextField(max_length=2000)),
                ('region', models.CharField(max_length=50)),
                ('unit_type', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('co2e_factor', models.DecimalField(decimal_places=4, max_digits=10)),
                ('co2', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('ch4', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('n2o', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
