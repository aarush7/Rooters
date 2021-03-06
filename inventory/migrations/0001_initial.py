# Generated by Django 3.0.5 on 2020-04-21 16:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusConfigModel',
            fields=[
                ('bus_config_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bus_make_type', models.CharField(choices=[('VOLV', 'Volvo'), ('SCAN', 'Scania'), ('MBEN', 'Mercedez Benz'), ('BBEN', 'Bharat Benz'), ('ALEY', 'Ashok Leyland'), ('TATA', 'Tata Motors'), ('VEER', 'Veera')], default=None, max_length=4)),
                ('bus_layer_type', models.CharField(choices=[('SIN', 'Single'), ('DOU', 'Double')], default=None, max_length=3)),
                ('bus_seat_structure_type', models.CharField(choices=[('2+2', 'Two Plus Two'), ('2+1', 'Two Plus One')], default=None, max_length=3)),
                ('bus_seat_type', models.CharField(choices=[('Seater', 'Seater'), ('Semi-Sleeper', 'Semi Sleeper'), ('Sleeper', 'Sleeper'), ('Seater-Sleeper', 'Seater Sleeper'), ('Semi-Sleeper + Sleeper', 'Sleeper Semi Sleeper')], default=None, max_length=30)),
                ('bus_climate_type', models.CharField(choices=[('A/C', 'Air Conditioned'), ('NAC', 'Non Air Conditioned')], default=None, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='BusModel',
            fields=[
                ('bus_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bus_name', models.CharField(max_length=50)),
                ('bus_plate_number', models.CharField(max_length=11)),
                ('bus_registration_date', models.DateField()),
                ('bus_registered_city_area', models.CharField(max_length=50)),
                ('bus_permit_type', models.CharField(choices=[('ALL', 'All India'), ('CON', 'Contract')], default=None, max_length=3)),
                ('bus_config', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.BusConfigModel')),
            ],
        ),
        migrations.CreateModel(
            name='BusSeatLayoutModel',
            fields=[
                ('seat_layout_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number_of_seats', models.IntegerField()),
                ('number_of_rows', models.IntegerField()),
                ('number_of_cols', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('city_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('city_state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RouteModel',
            fields=[
                ('route_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('route_distance', models.IntegerField()),
                ('destination_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='inventory.CityModel')),
                ('source_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_city', to='inventory.CityModel')),
            ],
        ),
        migrations.CreateModel(
            name='RouteScheduleModel',
            fields=[
                ('route_schedule_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('route_group', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dep_time', models.TimeField()),
                ('arr_time', models.TimeField()),
                ('order', models.IntegerField()),
                ('bus_config', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.BusConfigModel')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.RouteModel')),
            ],
        ),
        migrations.CreateModel(
            name='SeatDetailsModel',
            fields=[
                ('seat_details_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seat_number', models.CharField(max_length=3)),
                ('seat_fare', models.FloatField()),
                ('is_for_ladies', models.BooleanField()),
                ('seat_layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.BusSeatLayoutModel')),
            ],
        ),
        migrations.CreateModel(
            name='TripModel',
            fields=[
                ('trip_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dep_date', models.DateField()),
                ('arr_date', models.DateField()),
                ('dep_time', models.TimeField()),
                ('arr_time', models.TimeField()),
                ('available_seats', models.IntegerField()),
                ('route_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.RouteScheduleModel')),
                ('trip_bus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.BusModel')),
            ],
        ),
        migrations.CreateModel(
            name='SeatModel',
            fields=[
                ('seat_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('special', models.CharField(choices=[('LAD', 'Ladies'), ('HAN', 'Handicapped')], max_length=3)),
                ('seat_booking_status', models.CharField(choices=[('BKD', 'Booked'), ('BLK', 'Blocked'), ('OPN', 'Open')], max_length=3)),
                ('window_type', models.CharField(choices=[('WIN', 'Window'), ('AIL', 'Aisle')], max_length=3)),
                ('seat_detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.SeatDetailsModel')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.TripModel')),
            ],
        ),
        migrations.CreateModel(
            name='CityAreaModel',
            fields=[
                ('city_area_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city_area_name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.CityModel')),
            ],
        ),
        migrations.AddField(
            model_name='busconfigmodel',
            name='bus_seat_layout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.BusSeatLayoutModel'),
        ),
    ]
