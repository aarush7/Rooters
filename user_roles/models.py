from django.db import models
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
import uuid
from phone_field import PhoneField
#from django_simple_aes_field.fields import AESField
#from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models

#django.contrib.postgress
# Create your models here.
class address(models.Model):
    line1=models.CharField(max_length=150,blank=False)
    line2=models.CharField(max_length=150,blank=True)
    city=models.CharField(max_length=50,blank=False)
    state=models.CharField(max_length=30,blank=False)
    zipcode=models.IntegerField(blank=False)
    location = models.PointField(blank=True)
    class Meta:
        abstract=True

class cards_info(models.Model):
    card_info_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_on_card=models.CharField(max_length=50,blank=False)
    cc_number = CardNumberField(help_text='card number')
    cc_expiry = CardExpiryField(help_text='expiration date')
    cc_code = SecurityCodeField(help_text='security code')

class user(address):
    from .CONSTANTS import GENDER,ROLE

    user_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=25,blank=False)
    last_name=models.CharField(max_length=25,blank=False)
    email=models.EmailField(blank=False)
    contact=PhoneField(max_length=50,blank=False,help_text='Contact phone number')
    
    Gender=models.CharField(max_length=2,choices=GENDER.choices,blank=False)
    dob = models.DateField(max_length=8)
    
    def get_age(self):
        today = date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)
    age=property(get_age)
    

    role=models.CharField(max_length=3,choices=ROLE.choices,blank=False)


class customer(models.Model):
    from .CONSTANTS import REFER,SIGNUP,PAYMENT_METHOD

    customer_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_details=models.OneToOneField(user,on_delete=models.CASCADE,blank=False)
    customer_refferal_code=models.CharField(max_length=25,blank=True)
    referred_by=models.CharField(max_length=25,blank=True)
    
    referred_method=models.CharField(max_length=2,choices=REFER.choices,blank=True)
    
    sign_up_method=models.CharField(max_length=2,choices=SIGNUP.choices,blank=True)
    
    payment_method=models.CharField(max_length=3,choices=PAYMENT_METHOD.choices,blank=True)
    medical_history=models.CharField(max_length=50,blank=True)
    blood_group=models.CharField(max_length=3,blank=False)
    cards_list=models.ManyToManyField(cards_info)



class bankinfo(models.Model):
    account_holder_name=models.CharField(max_length=40,blank=False)
    bank_name=models.CharField(max_length=50,blank=False)
    account_no=models.IntegerField(blank=False)
    ifsc=models.CharField(max_length=20,blank=False)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    
class operator(models.Model):
    operator_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_details_id=models.OneToOneField(user,on_delete=models.CASCADE,blank=False)
    #operator_documents=ArrayField(models.BinaryField)
    company=models.CharField(max_length=30,blank=False)
    gst_no=models.CharField(max_length=20,blank=False)


class miscellaneous(models.Model):
    
    choices_qualification=(
        ('BELOW 10TH','BELOW 10TH'),
        ('10TH PASS','10TH PASS'),
        ('12TH PASS','12TH PASS'),
        ('GRADUATE','GRADUATE'),
        ('POST GRADUATE','POST GRADUATE')
    )
    qualification=models.CharField(max_length=30,choices=choices_qualification,blank=False)
    choices_languages=(
        ('Hindi','Hindi'),
        ('English','English'),
        ('Kannada','Kannada'),
        ('Malayalam','Malayalam'),
        ('Marathi','Marathi'),
        ('Tamil','Tamil'),
        ('Telugu','Telugu'),
        ('Urdu','Urdu'),
        ('Gujarati','Gujarati'),
        ('Bengali','Bengali')
    )
    languages=models.CharField(max_length=50,choices=choices_languages,blank=False,help_text='You can select multiple languages')
    joindate_wrtoperator=models.DateField(help_text='Enter Joining date with operator',blank=True)
    class Meta:
        abstract=True
class attendant(miscellaneous):
    attendant_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendant_details_id=models.OneToOneField(user,on_delete=models.CASCADE)
    #attendant_documents=ArrayField(models.BinaryField)
    attendant_salary=models.FloatField(max_length=7,blank=False)
    current_operator_id=models.ForeignKey(operator,on_delete=models.DO_NOTHING,blank=False)
class cleaner(miscellaneous):
    cleaner_id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    cleaner_details_id=models.OneToOneField(user,on_delete=models.CASCADE,blank=False)
    #cleaner_documents=ArrayField(models.BinaryField)
    cleaner_salary=models.FloatField(max_length=7,blank=False)
    current_operator_id=models.ForeignKey(operator,on_delete=models.DO_NOTHING,blank=False)
class driver(miscellaneous):
    driver_id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    driver_details_id=models.OneToOneField(user,on_delete=models.CASCADE,blank=False)
    lisence_no=models.IntegerField(blank=False)
    lisence_expiry_date=models.DateField()
    #driver_documents=ArrayField(models.BinaryField)
    driver_salary=models.FloatField(max_length=7,blank=False)
    current_operator_id=models.ForeignKey(operator,on_delete=models.DO_NOTHING,blank=False)


class rest_stop_contact(models.Model):
    rest_stop_contact_id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    owner_details=models.ForeignKey(user,on_delete=models.CASCADE,blank=False)
'''
class password(models.Model):
    password_id=
    user_id=models.OneToOneField(user,on_delete=models.CASCADE,blank=False)
'''   





  









