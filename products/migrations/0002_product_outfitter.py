# Generated by Django 3.0.8 on 2020-12-27 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='outfitter',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='products.Outfitter', verbose_name='Product outfitter'),
        ),
    ]
