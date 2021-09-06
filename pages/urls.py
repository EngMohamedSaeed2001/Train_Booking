from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('addTrain', views.addTrain, name='addTrain'),
    path('addTrip', views.addTrip, name='addTrip'),
    path('signUp', views.signUp, name='signUp'),
    path('Logout',views.Logout, name='Logout'),
    path('adminHome', views.adminHome, name='adminHome'),
    path('adminSignUp', views.adminSignUp, name='adminSignUp'),
    path('cancellation/<int:id>', views.cancellation, name='cancellation'),
    path('cancelBooking/<int:id>', views.cancelBooking, name='cancelBooking'),
    path('customerHome', views.customerHome, name='customerHome'),
    path('customerSignUp', views.customerSignUp, name='customerSignUp'),
    path('seats_search', views.seats_search, name='seats_search'),
    path('updateAdmin/<int:id>', views.updateAdmin, name='updateAdmin'),
    path('updateCustomer/<int:id>', views.updateCustomer, name='updateCustomer'),
    path('updateTrain/<int:id>', views.updateTrain, name='updateTrain'),
    path('updaateTrip/<int:id>', views.updateTrip, name='updateTrip'),
    path('viewTrain', views.viewTrain, name='viewTrain'),
    path('viewTrip', views.viewTrip, name='viewTrip'),
    path('viewCustomerTrips', views.viewCustomerTrips, name='viewCustomerTrips'),
    path('viewCustomer', views.viewCustomer, name='viewCustomer'),
    path('viewAdmin', views.viewAdmin, name='viewAdmin'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('ajax1', views.ajax1, name='ajax1'),
]
