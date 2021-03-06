# Generated by Django 2.1.7 on 2019-03-05 18:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('infoHistorial', '0010_auto_20190305_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]
