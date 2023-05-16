from .models import Vendor,Driver,Vehicle,Consignment

from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django import forms
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput

#from bootstrap_datepicker_plus import DatePickerInput

# Create the Vendor form class
class VendorForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Vendor
        # specify fields to be used
        fields = ['vn_nun', 'vn_code','vn_name','vn_contact','vn_phone_1','vn_phone_2','vn_email','vn_address']

# Create the Driver form class
class DriverForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Driver
        # specify fields to be used
        fields = ['dr_num', 'dr_code','dr_fname','dr_sname','dr_licence_no','dr_class','dr_licence_date',
                  'dr_fname','dr_sname','dr_gender','dr_dob','dr_start_date']
        widgets = {
            'dr_licence_date': widgets.DateInput(attrs={'type': 'date'}),
            'dr_dob': widgets.DateInput(attrs={'type': 'date'}),
            'dr_start_date': widgets.DateInput(attrs={'type': 'date'}),
        }

# Create the Vehicle form class
class VehicleForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Vehicle
        # specify fields to be used
        fields = ['vh_num', 'vh_code','vh_model','vh_make','vh_vn_num','vh_reg_num','vh_model','vh_make',
                  'vh_type','vh_reg_date']
        widgets = {
            'vh_reg_date': widgets.DateInput(attrs={'type': 'date'}),
        }

# Create the Consignment form class
class ConsignmentForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Consignment
        # specify fields to be used
        fields = ['cn_num', 'cn_code','cn_vh_num','cn_dr_num','cn_vn_num','cn_ref','cn_from','cn_type','cn_booked_date',
		'cn_pl_weight','cn_remarks','cn_comment','cn_confirmed','cn_status']
        widgets = {
            'cn_booked_date': widgets.DateInput(attrs={'type': 'date'}),
        }

class ConsignmentInForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Consignment
        # specify fields to be used
        fields = ['cn_num','cn_in_date','cn_in_weight','cn_in_units']
        widgets = {
            'cn_in_date': widgets.DateInput(attrs={'type': 'date'}),
        }

class ConsignmentOutForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Consignment
        # specify fields to be used
        fields = ['cn_num','cn_out_date','cn_out_wght','cn_out_units']
        widgets = {
            'cn_out_date': widgets.DateInput(attrs={'type': 'date'}),
        }
