from app.models import Feedback
from django import forms
from django.db.models import fields
from .models import Profile
from django.forms.fields import IntegerField
from .models import PurchaseModel, Purchase, ServiceRequest

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Full_Name', 'gender', 'mobile', 'pic','address')

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseModel
        fields = ('name','qty','total_amt')
        # widgets = {
        #     'qty':forms.HiddenInput(),
        # }

class PurchaseModel(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('user','equipment','price')
        # widgets = {
        #     'qty':forms.HiddenInput(),
        # 
        # }
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('durations', 'gender', 'age', 'request_for')
        

class FeedbackForm(forms.ModelForm):
    """Form definition for Feedback."""

    class Meta:
        """Meta definition for Feedbackform."""

        model = Feedback
        fields = ('name','email','phone','message')
    