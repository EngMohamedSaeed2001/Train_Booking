from django import forms
from django.contrib.auth.models import User

from .models import Train, Trip, Booking


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = [
            'trainName',
            'trainId',
            'numberOfSeats',
            'carriages',
            'status',
            'trip',

        ]
        widgets = {
            'trainName': forms.TextInput(attrs={'class': 'form-control'}),
            'trainId': forms.NumberInput(attrs={'class': 'form-control'}),
            'numberOfSeats': forms.NumberInput(attrs={'class': 'form-control'}),
            'carriages': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'trip': forms.Select(attrs={'class': 'form-control'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            'tripId',
            'seats',
            'date',
            'time',
            'sCity',
            'dCity',
        ]
        widgets = {
            'tripId': forms.NumberInput(attrs={'class': 'form-control'}),
            'seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': DateInput(),
            'time': TimeInput(),
            'sCity': forms.TextInput(attrs={'class': 'form-control'}),
            'dCity': forms.TextInput(attrs={'class': 'form-control'}),

        }


class AdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'username',
            'email',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'username',
            'email',
        ]



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'book_name',
            'bookId',
            'numberSeats',
            'carriag',
            'statu',
            'trips',

        ]
        widgets = {
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'bookId': forms.NumberInput(attrs={'class': 'form-control'}),
            'numberSeats': forms.NumberInput(attrs={'class': 'form-control'}),
            'carriag': forms.NumberInput(attrs={'class': 'form-control'}),
            'statu': forms.Select(attrs={'class': 'form-control'}),
            'trips': forms.Select(attrs={'class': 'form-control'}),
        }
