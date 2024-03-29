# Generated by Django 2.2 on 2019-06-15 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elite',
            old_name='departure',
            new_name='Passenger_name',
        ),
        migrations.AlterField(
            model_name='elite',
            name='Bus_number',
            field=models.CharField(choices=[('VJ6521', 'VJ6521'), ('VJ6522', 'VJ6522'), ('VJ6523', 'VJ6523'), ('VJ6524', 'VJ6524'), ('VJ6525', 'VJ6525'), ('VJ6526', 'VJ6526'), ('VJ6527', 'VJ6527'), ('VJ6528', 'VJ6528'), ('VJ6529', 'VJ6529'), ('VJ6530', 'VJ6530'), ('VJ6530', 'VJ6531'), ('VJ6532', 'VJ6532'), ('VJ6533', 'VJ6533'), ('VJ6534', 'VJ6534')], max_length=64),
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Passenger_name', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('Bus_number', models.CharField(choices=[('HY2300', 'HY2300'), ('HY2301', 'HY2301'), ('HY2302', 'HY2302'), ('HY2303', 'HY2303'), ('HY2304', 'HY2304'), ('HY2305', 'HY2305'), ('HY2306', 'HY2306'), ('HY2307', 'HY2307'), ('HY2308', 'HY2308'), ('HY2309', 'HY2309'), ('HY2310', 'HY2310'), ('HY2311', 'HY2311'), ('HY2312', 'HY2312'), ('HY2313', 'HY2313')], max_length=64)),
                ('Booking_id', models.IntegerField()),
                ('Bus_type', models.CharField(choices=[('Non-AC sleeper', 'Non-AC sleeper'), ('AC Multi Axle Semi sleeper', 'AC Multi Axle Semi sleeper'), ('AC seater', 'AC seater')], max_length=64)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busapp.Register')),
            ],
        ),
        migrations.CreateModel(
            name='Normal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Passenger_name', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('Bus_number', models.CharField(choices=[('GT4500', 'GT4500'), ('GT4501', 'GT4501'), ('GT4502', 'GT4502'), ('GT4503', 'GT4503'), ('GT4504', 'GT4504'), ('GT4505', 'GT4505'), ('GT4506', 'GT4506'), ('GT4507', 'GT4507'), ('GT4508', 'GT4508'), ('GT4509', 'GT4509'), ('GT4510', 'GT4510'), ('GT4511', 'GT4511')], max_length=64)),
                ('Booking_id', models.IntegerField()),
                ('Bus_type', models.CharField(choices=[('AC seater', 'AC seater'), ('Super Luxery', 'Super Luxery'), ('Deluxe', 'Deluxe')], max_length=64)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busapp.Register')),
            ],
        ),
    ]
