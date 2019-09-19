from django.contrib import admin
from .models import Register,Elite,Premium,Normal
from .forms import EliteForm,PremiumForm,NormalForm

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','Customer_name','Username','Password', 'Membership_type','Booking1_id']
admin.site.register(Register,RegisterAdmin)

class EliteAdmin(admin.ModelAdmin):
    list_display=['id','Booking_id','Passenger_name','Source','Destination','Bus_number','Booking_id','Bus_type']
admin.site.register(Elite, EliteAdmin)

class PremiumAdmin(admin.ModelAdmin):
    list_display=['id','User','Passenger_name','Source','Destination','Bus_number','Booking_id','Bus_type']
admin.site.register(Premium, PremiumAdmin)

class NormalAdmin(admin.ModelAdmin):
    list_display=['id','User','Passenger_name','Source','Destination','Bus_number','Booking_id','Bus_type']
admin.site.register(Normal, NormalAdmin)