# Generated by Django 3.0.8 on 2020-12-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit_name', models.CharField(max_length=60, verbose_name='Kit name')),
            ],
        ),
        migrations.AlterField(
            model_name='kit_info',
            name='goal',
            field=models.IntegerField(verbose_name='Goal number of kits'),
        ),
        migrations.AlterField(
            model_name='kit_info',
            name='project_name',
            field=models.CharField(max_length=60, verbose_name='Name of the project'),
        ),
        migrations.DeleteModel(
            name='kits',
        ),
        migrations.AddField(
            model_name='kit',
            name='kit_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kit.Kit_Info', verbose_name='General kit information'),
        ),
    ]
