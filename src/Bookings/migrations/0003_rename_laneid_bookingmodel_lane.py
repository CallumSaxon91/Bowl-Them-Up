# Generated by Django 3.2.9 on 2021-12-22 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0002_rename_customerid_bookingmodel_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingmodel',
            old_name='LaneId',
            new_name='Lane',
        ),
    ]