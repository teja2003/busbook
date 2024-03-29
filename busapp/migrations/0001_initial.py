# Generated by Django 2.2 on 2019-06-15 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=64)),
                ('Username', models.CharField(max_length=64)),
                ('Password', models.CharField(max_length=64)),
                ('Membership_type', models.CharField(max_length=64)),
                ('Booking1_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Elite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('departure', models.CharField(max_length=50)),
                ('Bus_number', models.CharField(choices=[('VJ6521', 'VJ6521')], max_length=64)),
                ('Booking_id', models.IntegerField()),
                ('Bus_type', models.CharField(choices=[('AC sleeper', 'AC sleeper'), ('Non-AC sleeper', 'Non-AC sleeper'), ('AC Multi Axle Semi sleeper', 'AC Multi Axle Semi sleeper'), ('AC seater', 'AC seater')], max_length=64)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busapp.Register')),
            ],
        ),
    ]
