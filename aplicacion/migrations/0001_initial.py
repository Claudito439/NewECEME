# Generated by Django 4.2.2 on 2023-08-30 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'División',
                'verbose_name_plural': 'Divisiones',
                'db_table': 'division',
            },
        ),
        migrations.CreateModel(
            name='Fuerza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Fuerza',
                'verbose_name_plural': 'Fuerzas',
                'db_table': 'fuerza',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('abreviacion', models.CharField(max_length=4, null=True)),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.division')),
                ('fuerza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.fuerza')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
                'db_table': 'unidad',
            },
        ),
        migrations.AddField(
            model_name='fuerza',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.pais'),
        ),
        migrations.AddField(
            model_name='division',
            name='fuerza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.fuerza'),
        ),
    ]