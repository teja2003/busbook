from django import forms
from .models import Register,Elite,Premium,Normal

class EliteForm(forms.ModelForm):
    class Meta:
        model = Elite
        fields = '__all__'
        exclude=('Booking_id',)
        depth=2

    def clean(self):
        cleaned_data=super().clean()
        bus_number=cleaned_data['Bus_number']
        query=Elite.objects.filter(Bus_number=bus_number)
        if query.exists():
            raise forms.ValidationError("This Seat is Already Booked")

class PremiumForm(forms.ModelForm):
    class Meta:
        model = Premium
        fields = '__all__'
        exclude=('Booking_id',)
        depth=2

    def clean(self):
        cleaned_data=super().clean()
        bus_number=cleaned_data['Bus_number']
        query=Premium.objects.filter(Bus_number=bus_number)
        if query.exists():
            raise forms.ValidationError("This Seat is Already Booked")

class NormalForm(forms.ModelForm):
    class Meta:
        model = Normal
        fields = '__all__'
        exclude=('Booking_id',)
        depth=2

    def clean(self):
        cleaned_data=super().clean()
        bus_number=cleaned_data['Bus_number']
        query=Normal.objects.filter(Bus_number=bus_number)
        if query.exists():
            raise forms.ValidationError("This Seat is Already Booked")