from django.db import models

# Create your models here.
class Vendor(models.Model):
	vn_nun		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying the vendor')
	vn_code		=	models.CharField(verbose_name='Assigned Code', max_length=100, help_text='A number/code by which vendor is identified by')
	vn_name		=	models.CharField(verbose_name='Vendor Name', max_length=200, help_text='The vendor s name')
	vn_contact	=	models.CharField(verbose_name='Contact Person', max_length=100, help_text='Vendor contact person')
	vn_phone_1	=	models.IntegerField(verbose_name='Phone',blank=True, null=True, help_text='Contact person phone number')
	vn_phone_2	=	models.IntegerField(verbose_name='Phone',blank=True, null=True, help_text='Contact person phone number')
	vn_email	=	models.EmailField(verbose_name='Email', max_length=200, help_text='Email address')
	vn_address	=	models.CharField(verbose_name='Physical Address', max_length=200, help_text='The vendor s Physical Address line')
	ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['vn_name']
		verbose_name = 'Vendor'

	def __str__(self):
		return self.vn_name

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.vn_name)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

class Driver(models.Model):
	dl_choices = (('1', 'Class 1'), ('2', 'Class 2'), ('3', 'Class 3'), ('4', 'Class 4'))
	gn_choices = (('1', 'Male'), ('2', 'Female'))

	dr_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying the driver')
	dr_code		=	models.CharField(verbose_name='Assigned Code',blank=True, null=True, max_length=100, help_text='A number/code by which driver is identified by')
	dr_licence_no	=	models.CharField(verbose_name='Licence No',blank=True, null=True, max_length=100, help_text='Driver s licence number')
	dr_class		=	models.CharField(verbose_name='Class',blank=True, null=True,choices=dl_choices, max_length=1, help_text='Class of vehicle driver licensed to drive')
	dr_licence_date	=	models.DateTimeField(verbose_name='Licensed Date',blank=True, null=True, help_text='Date drver obtained license')
	dr_fname		=	models.CharField(verbose_name='First Name', max_length=100, help_text='The driver s name')
	dr_sname		=	models.CharField(verbose_name='Surname', max_length=100, help_text='The driver s surname')
	dr_gender		=	models.CharField(verbose_name='Gender', choices=gn_choices,max_length=1, help_text='Gender of driver')
	dr_dob			=	models.DateTimeField(verbose_name='Date Born',blank=True, null=True, help_text='Date of birth')
	dr_start_date	=	models.DateTimeField(verbose_name='Start Date',blank=True, null=True, help_text='Date joined')
	ad_user_c		=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a		=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c		=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a		=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c		=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a		=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['dr_sname']
		verbose_name = 'Driver'

	def __str__(self):
		return self.dr_sname

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.dr_sname)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

class Vehicle(models.Model):
	ty_choices = (('1', 'Horse'), ('2', 'Truck'), ('3', 'Standard'))

	vh_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying the driver')
	vh_code		=	models.CharField(verbose_name='Assigned Code', max_length=100, help_text='A number/code by which veicle is identified by')
	vh_vn_num		=	models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='Vendor', help_text='Vendor')
	vh_reg_num		=	models.CharField(verbose_name='Reg. No',blank=True, null=True, max_length=100, help_text='Vehicle s registration number')
	vh_model		=	models.CharField(verbose_name='Model',blank=True, null=True, max_length=100, help_text='Vehicle Model')
	vh_make		=	models.CharField(verbose_name='Make',blank=True, null=True, max_length=100, help_text='Make of vehicle')
	vh_type		=	models.CharField(verbose_name='Type',choices=ty_choices, max_length=1, help_text='Vehicle type')
	vh_reg_date		=	models.DateTimeField(verbose_name='Reg. Date', help_text='Date registered')
	ad_user_c		=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a		=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c		=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a		=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c		=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a		=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['vh_reg_num']
		verbose_name = 'Vehicle'

	def __str__(self):
		return self.vh_reg_num

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.vh_reg_num)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

class Consignment(models.Model):
	st_choices = (('1', 'Planned'), ('2', 'Loaded'), ('3', 'In Transit'), ('4', 'Landed'))
	co_choices = (('1', 'Yes'), ('2', 'No'))
	co_type = (('1', 'Inbound'), ('2', 'Off-Take'))

	cn_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying the consignment')
	cn_code		=	models.CharField(verbose_name='Assigned Code', max_length=100, help_text='A number/code by which consignment is identified by')
	cn_vh_num		=	models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Vehicle', help_text='Vehicle')
	cn_dr_num		=	models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Driver', help_text='Driver')
	cn_vn_num		=	models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='Vendor', help_text='Vendor')
	cn_ref			=	models.CharField(verbose_name='Reference', max_length=100, help_text='Consignment s reference number')
	cn_from			=	models.CharField(verbose_name='Origin', max_length=100, help_text='Consignment s origin')
	cn_booked_date	=	models.DateTimeField(verbose_name='Booked Date', help_text='Date consignment is booked')
	cn_type			=	models.CharField(verbose_name='Type',default='1',choices=co_type,blank=True, null=True, max_length=1, help_text='Consignment type')
	cn_in_date		=	models.DateTimeField(verbose_name='Entry Date',blank=True, null=True, help_text='Entry date of truck entry')
	cn_pl_weight	=	models.DecimalField(verbose_name='Planned Weight',max_digits=15, decimal_places=2, default=0, help_text='Planned weight', null=True, blank=True)
	cn_in_weight	=	models.DecimalField(verbose_name='In Weight',max_digits=15, decimal_places=2, default=0, help_text='In weight', null=True, blank=True)
	cn_in_units		=	models.DecimalField(verbose_name='In Units',max_digits=15, decimal_places=2, default=0, help_text='In Units', null=True, blank=True)
	cn_out_date		=	models.DateTimeField(verbose_name='Exit Date',blank=True, null=True, help_text='Date and time of truck exit')
	cn_out_wght		=	models.DecimalField(verbose_name='Out Weight',max_digits=15, decimal_places=2, default=0, help_text='Out Weight', null=True, blank=True)
	cn_out_units	=	models.DecimalField(verbose_name='Out Units',max_digits=15, decimal_places=2, default=0, help_text='Out Units', null=True, blank=True)
	cn_remarks		=	models.CharField(verbose_name='Remarks',blank=True, null=True, max_length=200, help_text='Remarks on consignment')
	cn_comment		=	models.CharField(verbose_name='Comment',blank=True, null=True, max_length=200, help_text='Comment on consignment')
	cn_status		=	models.CharField(verbose_name='Status',default='1',choices=st_choices,blank=True, null=True, max_length=1, help_text='Consignment s status')
	cn_confirmed	=	models.CharField(verbose_name='Confirmed',default='N',choices=co_choices,blank=True, null=True, max_length=1, help_text='Consignment s confirmation status')
	ad_user_c		=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a		=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c		=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a		=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c		=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a		=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['cn_code']
		verbose_name = 'Consignment'

	def __str__(self):
		return self.cn_code

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.cn_code)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

