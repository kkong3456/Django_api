# Generated by Django 3.2 on 2021-05-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSAI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonbuNetIncrease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bugbu_bonbu', models.IntegerField()),
                ('dongbu_bonbu', models.IntegerField()),
                ('gangnam_bonbu', models.IntegerField()),
                ('daegu_gyeongbug', models.IntegerField()),
                ('busan_gyeongnam', models.IntegerField()),
                ('seobu_bonbu', models.IntegerField()),
                ('jeonnam_jeonbug', models.IntegerField()),
                ('jesu_bonbu', models.IntegerField()),
                ('chungnam_chungbug', models.IntegerField()),
            ],
            options={
                'db_table': 'bonbu_net_increase',
                'ordering': ['date'],
            },
        ),
        migrations.RenameModel(
            old_name='Rsai',
            new_name='JisaNetIncrease',
        ),
    ]
