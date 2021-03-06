# Generated by Django 3.0.5 on 2020-04-12 05:16

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_roles', '0001_initial'),
        ('promotions', '0001_initial'),
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('no_of_seats', models.IntegerField(max_length=5)),
                ('pnr', models.UUIDField(default='98B6B71B3', editable=False, unique=True)),
                ('flexibility', models.CharField(choices=[('CN', 'Cancellable'), ('RS', 'Reschedulable'), ('NR', 'Normal')], max_length=2)),
                ('payment_status', models.CharField(choices=[('SC', 'Success'), ('FL', 'Failed'), ('PB', 'Partially Book')], max_length=2)),
                ('total_amount', models.FloatField(max_length=100)),
                ('final_price', models.FloatField(max_length=100)),
                ('booking_method', models.CharField(choices=[('WA', 'Webapp'), ('PA', 'Phoneapp')], max_length=2)),
                ('booking_status', models.CharField(choices=[('CF', 'Confirmed'), ('CN', 'Cancelled')], max_length=2)),
                ('booked_by', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_roles.customer')),
                ('voucher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='promotions.voucher')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('serial_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_id', models.CharField(max_length=30)),
                ('transaction_amount', models.FloatField(max_length=100)),
                ('paid_to', models.CharField(blank=True, max_length=30)),
                ('paid_from', models.CharField(blank=True, max_length=30)),
                ('paid_on', models.DateTimeField(blank=True)),
                ('booking_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('passenger_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('contact', phone_field.models.PhoneField(help_text='Contact phone number', max_length=50)),
                ('Gender', models.CharField(choices=[('ML', 'Male'), ('FM', 'Female'), ('OT', 'Others')], max_length=2)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookidlink', to='booking.booking')),
                ('pnr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pnrlink', to='booking.booking')),
                ('seat_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory_app.SeatModel')),
                ('trip_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory_app.TripModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
