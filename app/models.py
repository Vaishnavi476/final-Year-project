from django.db import models

from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField, EmailField
from django.db.models.fields.related import ForeignKey
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator




#Create your models here.

duration_option = (
    ('1','1-Day'),
    ('2','2-Day'),
    ('3','3-Day'),
    ('4','4-Day'),
    ('5','5-Day'),
    ('6','6-Day'),
    ('7','7-Day'),
    ('8','8-Day'),
    ('9','9-Day'),
    ('10','10-Day')
    

    
)
gender_option = (
    ('M', 'Male'),
    ('F', 'Female')
)
age_option = (
    ('Teenager', '21 to 32'),
    ('elder', '33 to 44'),
)
phone_regex = RegexValidator(regex=r'^\d{10,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    Full_Name = models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=6,choices=gender_option, default='')
    email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15,validators=[phone_regex], default='')
    pic = models.ImageField(upload_to='users')
    update_on = models.DateTimeField(auto_now=True)
    address = models.TextField(default="not available")


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50, default='Machine_one')
    price = models.IntegerField(null=True)
    rent_price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='equipments')
    image_2 =  models.ImageField(upload_to='equipments')
    Description = models.TextField()
    availability = models.BooleanField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EquipmentRental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    rent_price = models.IntegerField(null=True)
    rent_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField(auto_now=True)
    Delivery_Address = models.TextField(max_length=500)
    is_date_expired = models.BooleanField(default=True)
    Fine = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.rent_price}"

class Human_Resource(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)
    address = models.TextField(max_length=500)
    helpertype = models.CharField(max_length=32)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=15,validators=[phone_regex])
    email = models.EmailField(blank=True)
    date_added = models.DateTimeField(auto_now=True) 
    is_available = models.BooleanField() 
    pic= models.ImageField(upload_to="hr",default="hr.png")


    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    equipment = models.ForeignKey(Equipment,on_delete=models.DO_NOTHING)
    price = models.IntegerField(null=True)
    is_payment_complete = models.BooleanField()
    date_purchase = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class PurchaseModel(models.Model):
    """Model definition for PurchaseModel."""
    buyer = models.ForeignKey(User,on_delete=CASCADE)
    name = CharField(max_length=30)
    qty = IntegerField(verbose_name="Quantity")
    total_amt = IntegerField(verbose_name="total amount")

    class Meta:
        """Meta definition for PurchaseModel."""

        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return f"{self.name} {self.qty}"

class Product(models.Model): 
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='products/') 
    price = models.FloatField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    hr = models.ForeignKey(Human_Resource, on_delete=models.CASCADE,related_name='hr_person')
    for_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='client')
    durations = models.CharField(max_length=100, choices=duration_option)
    gender = models.CharField(max_length=6, choices=gender_option,default='')
    age = models.CharField(max_length=30, choices=age_option,default='')
    request_for = models.TextField(default='')
    service_is_complete = models.BooleanField(default='True')

    

class Feedback(models.Model):
    
    name = CharField(max_length=50)
    email = EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    message = TextField()
    dated = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f'feedback from {self.name}'


class Contact(models.Model):
    con_name = models.CharField(max_length=20,null=True)
    con_mobile = models.CharField(max_length=30, null=True)
    con_email = models.CharField(max_length=10,null=True)
    con_purpose = models.CharField(max_length=15,null=True)
    message = models.TextField(default='')

    



    
    
    
