from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Vendor,Driver,Vehicle,Consignment

#Start Weights Admin Config

# Define the Vendor admin class
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vn_nun', 'vn_code','vn_name','vn_contact','vn_phone_1','vn_phone_2','vn_email','vn_address')

# Register the Vendor admin class with the associated model
admin.site.register(Vendor, VendorAdmin)

# Define the Driver admin class
class DriverAdmin(admin.ModelAdmin):
    list_display = ('dr_num', 'dr_code','dr_fname','dr_sname','dr_licence_no','dr_class','dr_licence_date','dr_fname','dr_sname','dr_gender','dr_dob','dr_start_date')

# Register the Driver admin class with the associated model
admin.site.register(Driver, DriverAdmin)

# Define the Vehicle admin class
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vh_num', 'vh_code','vh_model','vh_make','vh_vn_num','vh_reg_num','vh_model','vh_make','vh_type','vh_reg_date')

# Register the Vehicle admin class with the associated model
admin.site.register(Vehicle, VehicleAdmin)

# Define the Consignment admin class
class ConsignmentAdmin(admin.ModelAdmin):
    list_display = ('cn_num', 'cn_code','cn_vh_num','cn_dr_num','cn_vn_num','cn_ref','cn_from','cn_type','cn_booked_date','cn_in_date',
		'cn_pl_weight','cn_in_weight','cn_in_units','cn_out_date','cn_out_wght','cn_out_units','cn_remarks','cn_comment','cn_confirmed','cn_status')

# Register the Consignment admin class with the associated model
admin.site.register(Consignment, ConsignmentAdmin)

