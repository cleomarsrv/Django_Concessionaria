# Generated by Django 4.1.7 on 2023-04-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0008_carro_slugcarro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versao',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='carros'),
        ),
    ]
