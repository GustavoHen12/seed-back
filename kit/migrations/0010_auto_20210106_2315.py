# Generated by Django 3.0.8 on 2021-01-06 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0009_auto_20210106_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kit_product',
            name='kit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kit.Kit', verbose_name='Kit'),
        ),
    ]