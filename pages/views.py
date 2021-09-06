from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import TrainForm, TripForm, UserForm, AdminForm, BookingForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def addTrip(request):
    trainId = {
        'train': Train.objects.all(),
        'form1': TripForm(),
    }

    if request.method == "POST":
        add_Trip = TripForm(request.POST)
        if add_Trip.is_valid():
            add_Trip.save()
            return redirect('adminHome')

    return render(request, 'page/addTrip.html', trainId)


def addTrain(request):
    stat = {
        'train': Train.objects.all(),
        'trip': Trip.objects.all(),
        'form1': TrainForm(),
    }

    if request.method == "POST":
        add_Train = TrainForm(request.POST)
        if add_Train.is_valid():
            add_Train.save()
            return redirect('adminHome')

    return render(request, 'page/addTrain.html', stat)


def adminHome(request):
    return render(request, 'page/adminHome.html')


def adminSignUp(request):
    if request.method == 'POST':
        if not request.session.has_key('email'):
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password == password2:
                flag = True
                for obj in User.objects.all():
                    if obj.email == email:
                        flag = False
                        break
                if flag:
                    if username is not None or email is not None or password is not None:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        request.session['email'] = email
                        request.session['username'] = username
                        User.is_staff = True
                        user.save()
                        return redirect('adminHome')
                else:
                    messages.error(request, 'This email already exist!!')
            else:
                messages.error(request, 'Password and confirm Password not same!')
        else:
            return redirect('adminSignUp')
    return render(request, 'page/adminSignUp.html')


def cancellation(request, id):
    trip_delete = get_object_or_404(Trip, tripId=id)
    if request.method == 'POST':
        trip_delete.delete()
        return redirect('viewTrip')
    return render(request, 'page/cancellation.html')


def cancelBooking(request, id):
    book_delete = get_object_or_404(Train, trainId=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('viewCustomerTrips')

    context = {
        'train': book_delete,
    }
    return render(request, 'page/cancelBooking.html', context)


def customerHome(request):
    return render(request, 'page/customerHome.html')


def customerSignUp(request):
    if request.method == 'POST':
        if not request.session.has_key('email'):
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password == password2:
                flag = True
                for obj in User.objects.all():
                    if obj.email == email:
                        flag = False
                        break
                if flag:
                    if username is not None or email is not None or password is not None:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        request.session['email'] = email
                        request.session['username'] = username

                        user.save()
                        return redirect('customerHome')
                else:
                    messages.error(request, 'This email already exist!!')
            else:
                messages.error(request, 'Password and confirm Password not same!')
        else:
            return redirect('signUp')
    return render(request, 'page/customerSignUp.html')


def Home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if 'admin' in user.username:
                login(request, user)
                return redirect('adminHome')
            else:
                login(request, user)
                return redirect('customerHome')
        else:
            return redirect('Home')

    return render(request, 'page/Home.html')


def signUp(request):
    if request.method == 'POST':
        if not request.session.has_key('email'):
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password == password2:
                flag = True
                for obj in User.objects.all():
                    if obj.email == email:
                        flag = False
                        break
                if flag:
                    if username is not None or email is not None or password is not None:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        request.session['email'] = email
                        request.session['username'] = username
                        user.save()
                        return redirect('Home')
                else:
                    messages.error(request, 'This email already exist!!')
            else:
                messages.error(request, 'Password and confirm Password not same!')
        else:
            return redirect('signUp')

    return render(request, 'page/signUp.html')


def Logout(request):
    logout(request)
    return redirect('Home')


def seats_search(request):
    search = Train.objects.all()
    destCity = None
    srCity = None
    dat = None
    tim = None
    seat = None
    if 'dCity' in request.GET and 'sCity' in request.GET and 'date' in request.GET and 'time' in request.GET and 'seats' in request.GET:
        destCity = request.GET['dCity']
        srCity = request.GET['sCity']
        dat = request.GET['date']
        tim = request.GET['time']
        seat = request.GET['seats']

        if destCity and srCity and dat and tim and seat:
            search = search.filter(trip__dCity__icontains=destCity, trip__sCity__icontains=srCity,
                                   trip__date__icontains=dat, trip__time__icontains=tim, trip__seats__icontains=seat)

    context = {
        'search': search,
        'train': Train.objects.all(),
        'trip': Trip.objects.all(),
    }
    return render(request, 'page/seats_search.html', context)


def updateAdmin(request, id):
    try:
        admin_id = User.objects.get(id=id, email__icontains='admin@gmail.com')
    except User.DoesNotExist:
        admin_id = None
    if request.method == 'POST':
        admin_user = AdminForm(request.POST, instance=admin_id)
        if admin_user.is_valid():
            admin_user.save()
            return redirect('viewAdmin')
        messages.success(request, "Info saved successfully")
    else:
        admin_user = AdminForm(instance=admin_id)

    context = {
        'adminForm': admin_user,
    }
    return render(request, 'page/updateAdmin.html', context)


def updateCustomer(request, id):
    try:
        user_id = get_object_or_404(User, id=id, username__exact=auth.get_user(request).username)
    except User.DoesNotExist:
        user_id = None
    if request.method == 'POST':
        update_user = UserForm(request.POST, instance=user_id)
        if update_user.is_valid():
            update_user.save()
            return redirect('viewCustomer')
        messages.success(request, "Info saved successfully")
    else:
        update_user = UserForm(instance=user_id)

    context = {
        'userForm': update_user,
    }
    return render(request, 'page/updateCustomer.html', context)


def updateTrip(request, id):
    try:
        trip_id = get_object_or_404(Trip, tripId=id)
    except Trip.DoesNotExist:
        trip_id = None
    if request.method == 'POST':
        update_trip = TripForm(request.POST, instance=trip_id)
        if update_trip.is_valid():
            update_trip.save()
            return redirect('viewTrip')
    else:
        update_trip = TripForm(instance=trip_id)

    context = {
        'formTrip': update_trip,
        'seats': Seats.objects.all(),
        'train': Train.objects.all(),
        'trip': Trip.objects.all(),
    }
    return render(request, 'page/updateTrip.html', context)


def updateTrain(request, id):
    try:
        train_id = Train.objects.get(trainId=id)
    except Train.DoesNotExist:
        train_id = None
    if request.method == 'POST':
        update_train = TrainForm(request.POST, instance=train_id)
        if update_train.is_valid():
            update_train.save()
            return redirect('viewTrain')
        messages.success(request, "Train saved successfully")
    else:
        update_train = TrainForm(instance=train_id)

    context = {
        'form': update_train,
        'seats': Seats.objects.all(),
        'train': Train.objects.all(),
        'trip': Trip.objects.all(),
    }
    return render(request, 'page/updateTrain.html', context)


def viewTrain(request):
    context = {
        'seats': Seats.objects.all(),
        'train': Train.objects.all(),
        'trip': Trip.objects.all(),
    }
    return render(request, 'page/viewTrain.html', context)


def viewTrip(request):
    context = {
        'seats': Seats.objects.all(),
        'train': Train.objects.all(),
        'trip': Trip.objects.all(),
    }
    return render(request, 'page/viewTrip.html', context)



def viewCustomerTrips(request):
    '''
    for obj in Train.objects.get(trainName='lolo'):
        book = Booking(book_name=obj.trainName,bookId=obj.trainId,numberSeats=obj.numberOfSeats,carriag=obj.carriages,activate=obj.active,statu=obj.statu,trips=obj.trip)
        book.save()
    book.save()
    '''
    try:
        train_id = Train.objects.all()
    except Train.DoesNotExist:
        train_id = None

    context = {
        'train': train_id,
    }
    return render(request, 'page/viewCustomerTrips.html', context)


def viewAdmin(request):
    context = {
        'admin': User.objects.get(email__icontains='admin@gmail.com'),
    }
    return render(request, 'page/viewAdmin.html', context)


def viewCustomer(request):
    context = {
        'user': User.objects.get(username__exact=auth.get_user(request).username),
    }
    return render(request, 'page/viewCustomer.html', context)


def payment(request, id):
    try:
        trip_id = get_object_or_404(Train, trainId=id)
    except Train.DoesNotExist:
        trip_id = None

    context = {
        'trip': trip_id,
    }
    return render(request, 'page/payment.html', context)


def ajax1(request):
    return render(request, 'page/ajax1.html')
