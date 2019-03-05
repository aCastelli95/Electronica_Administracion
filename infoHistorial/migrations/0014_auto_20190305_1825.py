# Generated by Django 2.1.7 on 2019-03-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoHistorial', '0013_auto_20190305_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='chasis',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='control_remoto',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='display',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='firmware',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fuente',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='main',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='modelo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='modelo_equivalente',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='modo_servicio',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
