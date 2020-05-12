from django.db import models
import uuid
from phone_field import PhoneField
from promotions import models as voucher_md
from user_roles.models import customer
from inventory_app.models import TripModel,SeatModel


# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class booking(TimeStampMixin):
    from .CONSTANTS import FLEX,BOOKING_METHOD,BOOKING_STATUS,PAY
    booking_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    no_of_seats=models.IntegerField(blank=False)
    pnr=models.UUIDField(default=uuid.uuid4().hex[0:9].upper(),editable=False,unique=True)
    #models.CharField(max_length=20,blank=False)

    flexibility=models.CharField(max_length=2,choices=FLEX.choices,blank=False)
    
    payment_status=models.CharField(max_length=2,choices=PAY.choices,blank=False)
    total_amount=models.FloatField(max_length=100,blank=False)
    final_price=models.FloatField(max_length=100,blank=False)
    voucher_id=models.ForeignKey(voucher_md.voucher,on_delete=models.DO_NOTHING,blank=True,null=True)
    booked_by=models.OneToOneField(customer,on_delete=models.DO_NOTHING,blank=True)
    
    booking_method=models.CharField(max_length=2,choices=BOOKING_METHOD.choices,blank=False)
   
    booking_status=models.CharField(max_length=2,choices=BOOKING_STATUS.choices,blank=False)

class transaction(TimeStampMixin):
    serial_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id=models.CharField(max_length=30,blank=False)
    transaction_amount=models.FloatField(max_length=100,blank=False)
    paid_to=models.CharField(max_length=30,blank=True)
    paid_from=models.CharField(max_length=30,blank=True)
    paid_on=models.DateTimeField(blank=True)
    booking_id=models.OneToOneField(booking, on_delete=models.CASCADE)


    

class passenger(TimeStampMixin):
    from .CONSTANTS import GENDER
    passenger_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=25,blank=False)
    last_name=models.CharField(max_length=25,blank=False)
    email=models.EmailField(blank=False)
    contact=PhoneField(max_length=50,blank=False,help_text='Contact phone number')
    
    Gender=models.CharField(max_length=2,choices=GENDER.choices,blank=False)
    seat_id=models.OneToOneField(SeatModel,on_delete= models.DO_NOTHING)
    trip_id=models.OneToOneField(TripModel,on_delete=models.DO_NOTHING)
    pnr=models.ForeignKey(booking,related_name="pnrlink",on_delete=models.DO_NOTHING)
    booking_id=models.ForeignKey(booking,related_name="bookidlink",on_delete=models.CASCADE)


    
    


















    