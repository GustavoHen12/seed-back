# Generated by Django 3.0.8 on 2021-01-13 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0011_auto_20210113_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit',
            name='kit_info',
        ),
        migrations.AddField(
            model_name='kit',
            name='goal',
            field=models.IntegerField(default=0, verbose_name='Goal number of kits'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kit',
            name='img',
            field=models.ImageField(default='defaultImage.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='kit',
            name='project',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='kit.Project', verbose_name='Name of the project'),
        ),
        migrations.AlterField(
            model_name='kit_product',
            name='kit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kit.Kit', verbose_name='Kit'),
        ),
        migrations.DeleteModel(
            name='Kit_Info',
        ),
    ]
