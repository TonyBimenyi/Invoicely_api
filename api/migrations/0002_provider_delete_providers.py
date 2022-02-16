# Generated by Django 4.0.2 on 2022-02-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('phone', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Providers',
        ),
    ]