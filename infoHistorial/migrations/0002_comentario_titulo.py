# Generated by Django 2.0.13 on 2019-02-23 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoHistorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='titulo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
