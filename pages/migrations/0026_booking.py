# Generated by Django 3.2.5 on 2021-07-18 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_auto_20210717_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.train')),
            ],
        ),
    ]
