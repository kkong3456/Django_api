# Generated by Django 3.2 on 2021-04-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rsai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jisa', models.CharField(max_length=20)),
                ('day', models.DateField(verbose_name='일자')),
                ('sales', models.CharField(max_length=30)),
                ('etc', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['jisa'],
            },
        ),
    ]