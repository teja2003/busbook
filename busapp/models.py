from django.db import models
import datetime        

# Create your models here.
Bus1=[
    ('VJ6531-LB','VJ6531-LB'),
    ('VJ6532-UB','VJ6532-UB'),
    ('VJ6533-LB','VJ6523-LB'),
    ('VJ6534-UB','VJ6524-UB'),
    ('GT4605','GT4605'),
    ('GT4606','GT4606'),
    ('GT4607','GT4607'),
    ('WG6728-UB','WG6728-UB'),
    ('WG6729-LB','WG6729-LB'),
    ('HY4755','HY4755'),
    ('HY4756','HY4756'),
    ('HY4757','HY4757'),
    ('HY4758','HY4758'),
    ('HY4759','HY4759'),
    ('HY4760','HY4760'),
    ('HY4761','HY4761'),
    ('WG6730-UB','WG6730-UB'),
    ('WG6731-LB','WG6731-LB'),
    ('WG6732-UB','WG6732-UB'),
    ('WG6733-LB','WG6733-LB'),
    ('WG6734-UB','WG6734-UB'),
    ('GT4908','GT4908'),
    ('GT4909','GT4909'),
    ('GT4910','GT4910'),
    ('GT4911','GT4911'),
    ('VJ6535-LB','VJ6525-LB'),
    ('VJ6536-UB','VJ6526-UB'),
    ('VJ6537-LB','VJ6527-LB'),
    ('VJ6538-UB','VJ6528-UB'),
    ('VJ6539-LB','VJ6529-LB'),
    ('VJ6540-UB','VJ6530-UB'),
    ('VJ6541-LB','VJ6531-LB'),
    ('VJ6542-UB','VJ6532-UB'),
    ('VJ6543-LB','VJ6533-LB'),
    ('VJ6544-UB','VJ6534-UB'),
]

Bus2=[
    ('WG6621-LB','WG6621-LB'),
    ('WG6622-UB','WG6622-UB'),
    ('WG6623-LB','WG6623-LB'),
    ('WG6624-UB','WG6624-UB'),
    ('WG6625-LB','WG6625-LB'),
    ('WG6626-UB','WG6626-UB'),
    ('GT4505','GT4505'),
    ('GT4506','GT4506'),
    ('GT4507','GT4507'),
    ('GT4508','GT4508'),
    ('VJ6637-LB','VJ6627-LB'),
    ('VJ6638-UB','VJ6628-UB'),
    ('VJ6639-LB','VJ6629-LB'),
    ('HY4555','HY4555'),
    ('HY4556','HY4556'),
    ('HY4557','HY4557'),
    ('HY4558','HY4558'),
    ('HY4559','HY4559'),
    ('HY4560','HY4560'),
    ('HY4561','HY4561'),
    ('VJ6640-UB','VJ6630-UB'),
    ('VJ6641-LB','VJ6631-LB'),
    ('VJ6642-UB','VJ6632-UB'),
    ('VJ6643-LB','VJ6633-LB'),
    ('VJ6644-UB','VJ6634-UB'),
    ('GT4509','GT4509'),
    ('GT4510','GT4510'),
    ('GT4511','GT4511'),
    ('WG6627-LB','WG6627-LB'),
    ('WG6628-UB','WG6628-UB'),
    ('WG6629-LB','WG6629-LB'),
    ('WG6630-UB','WG6630-UB'),
    ('WG6631-LB','WG6631-LB'),
    ('WG6632-UB','WG6632-UB'),
    ('WG6633-LB','WG6633-LB'),
    ('WG6634-UB','WG6634-UB'),

]

Bus3=[
    ('GT4400','GT4400'),
    ('GT4401','GT4401'),
    ('GT4402','GT4402'),
    ('GT4403','GT4403'),
    ('VJ6138-UB','VJ6128-UB'),
    ('VJ6139-LB','VJ6129-LB'),
    ('VJ6140-UB','VJ6130-UB'),
    ('WG6628-UB','WG6628-UB'),
    ('HY4565','HY4565'),
    ('HY4566','HY4566'),
    ('HY4567','HY4567'),
    ('HY4568','HY4568'),
    ('HY4569','HY4569'),
    ('HY4580','HY4580'),
    ('HY4581','HY4581'),
    ('WG6929-LB','WG6929-LB'),
    ('WG6930-UB','WG6930-UB'),
    ('WG6931-LB','WG6931-LB'),
    ('WG6932-UB','WG6932-UB'),
    ('WG6933-LB','WG6933-LB'),
    ('VJ6521-LB','VJ6521-LB'),
    ('VJ6522-UB','VJ6522-UB'),
    ('VJ6523-LB','VJ6523-LB'),
    ('VJ6524-UB','VJ6524-UB'),
    ('GT4804','GT4804'),
    ('GT4805','GT4805'),
    ('GT4806','GT4806'),
    ('GT4807','GT4807'),
    ('GT4808','GT4808'),
    ('GT4809','GT4809'),
    ('GT4810','GT4810'),
    ('GT4811','GT4811'),
]

CHOICES = [('AC sleeper', 'AC sleeper'),
   ('Non-AC sleeper', 'Non-AC sleeper'),
   ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
   ('AC seater','AC seater')]

CHOICES1 = [('Non-AC sleeper', 'Non-AC sleeper'),
   ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
   ('AC seater','AC seater')]

CHOICES2 = [('AC seater','AC seater'),
('Super Luxery','Super Luxery'),
('Deluxe','Deluxe')]


class Register(models.Model):
    Customer_name= models.CharField(max_length=64)
    Username= models.CharField(max_length=64)
    Password= models.CharField(max_length=64)
    Membership_type=models.CharField(max_length=64)
    Booking1_id=models.IntegerField()

    def __str__(self):
        return str(self.Booking1_id)

class Elite(models.Model): 
    Booking_id= models.ForeignKey(Register, on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=50)
    Source=models.CharField(max_length=50)
    Destination=models.CharField(max_length=50)
    Bus_number=models.CharField(max_length=64,choices=Bus1)
    Booking_id=models.IntegerField()
    Bus_type=models.CharField(max_length=64, choices=CHOICES,)
    # Departure_time=models.datetime(datetime)
    def __str__(self):
        return self.Bus_number

class Premium(models.Model):  
    User = models.ForeignKey(Register, on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=50)
    Source=models.CharField(max_length=50)
    Destination=models.CharField(max_length=50)
    Bus_number=models.CharField(max_length=64,choices=Bus2,)
    Booking_id=models.IntegerField()
    Bus_type=models.CharField(max_length=64, choices=CHOICES1,)

class Normal(models.Model):  
    User = models.ForeignKey(Register, on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=50)
    Source=models.CharField(max_length=50)
    Destination=models.CharField(max_length=50)
    Bus_number=models.CharField(max_length=64,choices=Bus3,)
    Booking_id=models.IntegerField()
    Bus_type=models.CharField(max_length=64, choices=CHOICES2,)