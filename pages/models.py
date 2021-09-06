from django.db import models

# Create your models here.

class Trip(models.Model):
    sCity = models.CharField(max_length=50)
    dCity = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField()
    tripId =models.IntegerField()

    def __str__(self):
        return str(self.tripId)

class Train(models.Model):
    statu = [
        ("available", "available"),
        ("unavailable", "unavailable"),
    ]

    trainName = models.CharField(max_length=50)
    trainId = models.IntegerField()
    numberOfSeats = models.IntegerField()
    carriages = models.IntegerField()
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=statu, blank=True,null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.trainName

class Seats(models.Model):
    sourceCity = models.CharField(max_length=50)
    destinationCity = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    available_seats = models.ForeignKey(Train, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.available_seats.trainName)


class Booking(models.Model):
    statu = [
        ("available", "available"),
        ("unavailable", "unavailable"),
    ]
    book_name =models.CharField(max_length=50,default=True)
    bookId = models.IntegerField(default=True)
    numberSeats = models.IntegerField(default=True)
    carriag = models.IntegerField(default=True)
    activate = models.BooleanField(default=True)
    statu = models.CharField(max_length=50, choices=statu, blank=True, null=True)
    trips = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.book_name


class client(models.Model):
    user = models.ForeignKey(Booking, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default=True)

    def __str__(self):
        return self.username