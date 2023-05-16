
from .models import Vendor,Driver,Vehicle,Consignment

from .forms import VendorForm,DriverForm,VehicleForm,ConsignmentForm,ConsignmentInForm,ConsignmentOutForm

from django.http import HttpResponse
from django_globals import globals
import json

#Imports for table
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
#from .tables import TransHTMxTable
from .filters import ConsignFilter
import django_tables2 as tables

#End imports for table

import datetime
import csv, io
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from django.db.models import Sum, F,Avg, Max, Min,Count,Q
from django.core.mail import EmailMessage

from django.views.generic import ListView, DetailView

from django.conf import settings
import csv,io
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Round

#from django.http import HttpResponse
import getpass
from os import environ, getcwd
from decimal import *
#from bootstrap_datepicker_plus import DatePickerInput

# Getting variables for filtering transactions by user groups

def HomeIndexView(Request):
    template = 'homeindex.html'
    context = {}

    return render (Request, template, context)

def ConsListView(request):
    pl_total = 0
    in_total = 0
    out_total = 0
    net_total = 0

    cons_list = Consignment.objects.values('cn_num', 'cn_code', 'cn_booked_date', 'cn_pl_weight', 'cn_type',
                                            'cn_in_date','cn_out_date', 'cn_in_weight', 'cn_out_wght').order_by('cn_booked_date',
                                                                                                   'cn_type')
    cons_list1 = ConsignFilter(request.GET, queryset=cons_list)
    pl_total = cons_list1.qs.aggregate(pl_total=Sum('cn_pl_weight'))
    in_total = cons_list1.qs.aggregate(in_total=Sum('cn_in_weight'))
    out_total = cons_list1.qs.aggregate(out_total=Sum('cn_out_wght'))

    #net_total = (in_total - out_total)

    context = {'filter':
    cons_list1, 'pl_total': pl_total, 'in_total': in_total, 'out_total': out_total, 'net_total': net_total}

    return render(request, 'star_track/reports/cons_rtp1.html', context)

# home view for Vendor. Vendors are displayed in a list
class VendorIndexView(ListView):
    template_name = 'star_track/vendor/index.html'
    context_object_name = 'Vendor_list'

    def get_queryset(self):
        return Vendor.objects.all()

# Detail view (view Vendor detail)
class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'star_track/vendor/vendor-detail.html'

# New Vendor view (Create new Vendor)
def VendorView(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vendor')
    form = VendorForm()
    return render(request, 'star_track/vendor/vendor.html', {'form': form})

# Edit a Vendor
def EditVendor(request, pk, template_name='star_track/vendor/edit.html'):
    vendor = get_object_or_404(Vendor, pk=pk)
    form = VendorForm(request.POST or None, instance=vendor)
    if form.is_valid():
        form.save()
        return redirect('vendor')
    return render(request, template_name, {'form': form})

# Delete Vendor
def DeleteVendor(request, pk, template_name='star_track/vendor/confirm_delete.html'):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor')
    return render(request, template_name, {'object': vendor})

# home view for Vehicle. Vehicles are displayed in a list
class VehicleIndexView(ListView):
    template_name = 'star_track/vehicle/index.html'
    context_object_name = 'Vehicle_list'

    def get_queryset(self):
        return Vehicle.objects.all()

# Detail view (view Vehicle detail)
class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'star_track/vehicle/vehicle-detail.html'

# New Vehicle view (Create new Vehicle)
def VehicleView(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehicle')
    form = VehicleForm()
    return render(request, 'star_track/vehicle/vehicle.html', {'form': form})

# Edit a Vehicle
def EditVehicle(request, pk, template_name='star_track/vehicle/edit.html'):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('vehicle')
    return render(request, template_name, {'form': form})

# Delete Vehicle
def DeleteVehicle(request, pk, template_name='star_track/vehicle/confirm_delete.html'):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle')
    return render(request, template_name, {'object': vehicle})

# home view for Driver. Driver are displayed in a list
class DriverIndexView(ListView):
    template_name = 'star_track/driver/index.html'
    context_object_name = 'Driver_list'

    def get_queryset(self):
        return Driver.objects.all()

# Detail view (view Driver detail)
class DriverDetailView(DetailView):
    model = Driver
    template_name = 'star_track/driver/driver-detail.html'

# New Driver view (Create new Driver)
def DriverView(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('driver')
    form = DriverForm()
    return render(request, 'star_track/driver/driver.html', {'form': form})

# Edit a Driver
def EditDriver(request, pk, template_name='star_track/driver/edit.html'):
    driver = get_object_or_404(Driver, pk=pk)
    form = DriverForm(request.POST or None, instance=driver)
    if form.is_valid():
        form.save()
        return redirect('driver')
    return render(request, template_name, {'form': form})

# Delete Driver
def DeleteDriver(request, pk, template_name='star_track/driver/confirm_delete.html'):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver')
    return render(request, template_name, {'object': driver})

# home view for Consignment. Consignment are displayed in a list
class ConsignmentIndexView(ListView):
    template_name = 'star_track/consignment/index.html'
    context_object_name = 'Consignment_list'

    def get_queryset(self):
        return Consignment.objects.all()

# Detail view (view Consignment detail)
class ConsignmentDetailView(DetailView):
    model = Consignment
    template_name = 'star_track/consignment/consignment-detail.html'

# New Consignment view (Create new Consignment)
def ConsignmentView(request):
    if request.method == 'POST':
        form = ConsignmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('consignment')
    form = ConsignmentForm()
    return render(request, 'star_track/consignment/consignment.html', {'form': form})

# Edit a Consignment
def EditConsignment(request, pk, template_name='star_track/consignment/edit.html'):
    consignment = get_object_or_404(Consignment, pk=pk)
    form = ConsignmentForm(request.POST or None, instance=consignment)
    if form.is_valid():
        form.save()
        return redirect('consignment')
    return render(request, template_name, {'form': form})

def EditConsignmentIn(request, pk, template_name='star_track/consignment/edit.html'):
    import time
    import serial
    import re

    serialPort = serial.Serial(port="COM4", baudrate=115200,
                               bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    serialString = ""  # Used to hold data coming over UART

    while (1):

        # Wait until there is data waiting in the serial buffer
        if (serialPort.in_waiting > 0):
            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()

            # Print the contents of the serial data
            print(serialString.decode('Ascii'))

            # Tell the device connected over the serial port that we recevied the data!
            # The b at the beginning is used to indicate bytes!
            serialPort.write(b"Thank you for sending data \r\n")

    #ser = serial.Serial(
     #   port='COM3',
      #  baudrate=9600,
       # timeout=None,
        #parity=serial.PARITY_EVEN,
        #stopbits=serial.STOPBITS_ONE,
        #bytesize=serial.SEVENBITS
    #)
    #ser.isOpen()
    #while 1 :
     #       bytesToRead = ser.inWaiting()
      #      data = ser.read(bytesToRead)
       #     time.sleep(1)
        #    print(str(data))

    weight_var = 0
    #weight_var = data
    units_var = 0
    units_var = 1
    consignment = get_object_or_404(Consignment, pk=pk)
    form = ConsignmentInForm(request.POST or None, instance=consignment,
                             initial={'cn_in_weight': weight_var,'cn_in_units': units_var})
    if form.is_valid():
        form.save()
        return redirect('consignment')
    return render(request, template_name, {'form': form})

def EditConsignmentOut(request, pk, template_name='star_track/consignment/edit.html'):
    weight_var = 0
    weight_var = 155.50
    units_var = 0
    units_var = 1
    consignment = get_object_or_404(Consignment, pk=pk)
    form = ConsignmentOutForm(request.POST or None, instance=consignment,
                             initial={'cn_out_wght': weight_var,'cn_out_units': units_var})
    if form.is_valid():
        form.save()
        return redirect('consignment')
    return render(request, template_name, {'form': form})

# Delete Consignment
def DeleteConsignment(request, pk, template_name='star_track/consignment/confirm_delete.html'):
    consignment = get_object_or_404(Consignment, pk=pk)
    if request.method == 'POST':
        consignment.delete()
        return redirect('consignment')
    return render(request, template_name, {'object': consignment})

# Visualization Views
def g_position(request):

        dataset = Consignment.objects.values('cn_booked_date__month').annotate(
            pl_sum=Sum('cn_pl_weight'),in_sum=Sum('cn_in_weight'),out_sum=Sum('cn_out_wght')).order_by('cn_booked_date__month')

        periods = list()
        pl_series_data = list()
        rec_series_data = list()
        out_series_data = list()

        for entry in dataset:
            periods.append('%s Period' % entry['cn_booked_date__month'])

            pl = entry['pl_sum']
            if pl is None:
                pl = 0
            pl = float(pl)

            in_sum = entry['in_sum']
            if in_sum is None:
                in_sum = 0
            in_sum = abs(float(in_sum))

            out_sum = entry['out_sum']
            if out_sum is None:
                out_sum = 0
            out_sum = abs(float(out_sum))

            print(in_sum)
            print(pl)
            rec_sum = 0
            rec_sum =(in_sum - out_sum)

            pl_series_data.append(pl)
            rec_series_data.append(rec_sum)
            out_series_data.append(out_sum)

        pl_series = {
            'name': 'Planned',
            'data': pl_series_data,
            'color': 'purple'
        }

        rec_series = {
            'name': 'Receipts',
            'data': rec_series_data,
            'color': 'green'
        }

        out_series = {
            'name': 'OutBound',
            'data': out_series_data,
            'color': 'blue'
        }

        chart = {
            'chart': {'type': 'column'},
            'title': {'text': 'Load Dashboard'},
            'xAxis': {'periods': periods,'type': "category"},
            'series': [pl_series, rec_series,out_series]
        }

        dump = json.dumps(chart, cls=DecimalEncoder)

        return render(request, 'star_track/reports/charts/g_position.html', {'chart': dump})

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        #  if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)