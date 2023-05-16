from django.urls import path, include
from . import views

from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
#path('',views.index)
    path('accounts/', include('django.contrib.auth.urls')),
    ]

#URLCONFIG
urlpatterns = [
   path('', views.HomeIndexView, name='homepage'),
  #  path('members', views.EmpHomeView, name='members'),
   # path('geoparams', views.GeoHomeView, name='geoparams'),
    #path('genparams', views.ParaHomeView, name='genparams'),
    #path('trans', views.TransHomeView, name='trans'),
    #path('farmproj', views.FarmProjHomeView, name='farmproj'),

   path('addvendor', views.VendorView, name='addvendor'),
   path('vendordetail/str<pk>/', views.VendorDetailView.as_view(), name='vendordetail'),
   path('editvendor/<str:pk>/', views.EditVendor, name='editvendor'),
   path('vendor/', views.VendorIndexView.as_view(), name='vendor'),
   path('deletevendor/<str:pk>/', views.DeleteVendor, name='deletevendor'),

   path('addvehicle', views.VehicleView, name='addvehicle'),
   path('vehicledetail/str<pk>/', views.VehicleDetailView.as_view(), name='vehicle'),
   path('editvehicle/<str:pk>/', views.EditVehicle, name='editvehicle'),
   path('vehicle/', views.VehicleIndexView.as_view(), name='vehicle'),
   path('deletevehicle/<str:pk>/', views.DeleteVehicle, name='deletevehicle'),

   path('adddriver', views.DriverView, name='adddriver'),
   path('driverdetail/str<pk>/', views.DriverDetailView.as_view(), name='driverdetail'),
   path('editdriver/<str:pk>/', views.EditDriver, name='editdriver'),
   path('driver/', views.DriverIndexView.as_view(), name='driver'),
   path('deletedriver/<str:pk>/', views.DeleteDriver, name='deletedriver'),

   path('addconsignment', views.ConsignmentView, name='addconsignment'),
   path('consignmentdetail/str<pk>/', views.ConsignmentDetailView.as_view(), name='consignment'),
   path('editconsignment/<str:pk>/', views.EditConsignment, name='editconsignment'),
   path('editconsignmentin/<str:pk>/', views.EditConsignmentIn, name='editconsignmentin'),
   path('editconsignmentout/<str:pk>/', views.EditConsignmentOut, name='editconsignmentout'),
   path('consignment/', views.ConsignmentIndexView.as_view(), name='consignment'),
   path('deleteconsignment/<str:pk>/', views.DeleteConsignment, name='deleteconsignment'),

#Reports
    path('g_position', views.g_position, name='g_position'),
    path('conslist', views.ConsListView, name='conslist'),

]

urlpatterns += [
        path('accounts/', include('django.contrib.auth.urls')),
        ]
