from django.shortcuts import render,redirect
from app_booking.models import Doctor,Patient,booking

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

# def signup(request):
#     return render(request,'signup.html')

def booking_page(request):

    data = Doctor.objects.all()  # getting all the  datas from db to 'data'
    context = {"data": data}  # passing all the data into context in the form of dictionary
    # print(context)
# inserting data to db-
    if request.method == "POST":
        dname = request.POST.get('d_name')
        pname = request.POST.get('p_name')
        date = request.POST.get('date')
        # time = request.POST.get('time')
        selected_time = request.POST.get('selected_time')
        contact=request.POST.get('contactno')
        message = request.POST.get('message')
        # print(pname)
        query = booking(d_name=dname, p_name=pname, date=date, time=selected_time, contactno=contact, message=message)
        query.save()
        return redirect("/") # redirect to homepage,
    return render(request, 'booking.html', context) # this context is  for : available doctor's name list

def appo_list(request):
    print("hai")
    data = booking.objects.all()  # getting all the  datas from db to 'data'
    context = {'data': data}
    # print(context)
    return render(request, 'appointment.html',context)

def doctors_page(request):
    doctor = Doctor.objects.all()
    return render(request, 'doctors.html', {'data': doctor})


def department_page(request):

    return render(request,'department.html')

def contactus_page(request):
    return render(request,'contactus.html')

def aboutus_page(request):
    return render(request,'aboutus.html')

def Login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd = request.POST.get('pwd')

        # user=authenticate(username=uname,password=pwd) # correct
        user = authenticate(request,username=uname, password=pwd)
        if user is not None:
            login(request,user)
            return  redirect('appointments')
        else:
            return HttpResponse('Error,User does not exist')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
