# Generated by Django 2.2.6 on 2020-03-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
