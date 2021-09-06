# Generated by Django 3.2.5 on 2021-07-19 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_rename_train_booking_train_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='train_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='activate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='bookId',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='book_name',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='booking',
            name='carriag',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='numberSeats',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='statu',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='trips',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.trip'),
        ),
    ]
