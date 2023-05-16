from django import forms
from .models import Consignment
import django_filters
#from decimal import Decimal
from django.db.models import Q


class ConsignFilter(django_filters.FilterSet):

    class Meta:
        model = Consignment
        fields = ['cn_booked_date','cn_vn_num','cn_vh_num']