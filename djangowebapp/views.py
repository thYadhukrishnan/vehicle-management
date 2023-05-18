from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

def about(request):
    return HttpResponse("About page")

def course(request,id):
    return HttpResponse(id)

def home(request):
    # data={
    #     'title':'Home Page',
    #     'list':['java','php','python']
    # }

    vehicledata=Service.objects.all()

    data={
        'data':vehicledata
    }
    
    return render(request,"home.html",data)

def login(request):
    return render(request,"login.html")

def create(request):

    if request.method == 'POST':

        data=request.POST
        vehicle_number=data.get('number')
        vehicle_type=data.get('type')
        vehicle_model=data.get('model')
        vehicle_desc=data.get('desc')
        print(vehicle_type)

        service = Service(
            vehicle_number=vehicle_number,
            vehicle_type=vehicle_type,
            vehicle_model=vehicle_model,
            vehicle_desc=vehicle_desc
        )
        service.save()

        return redirect('home')


    return render(request,"create.html")

def delete(request,id):
    vehicle = get_object_or_404(Service, id=id)
    print(vehicle.vehicle_number)
    if vehicle:
        vehicle.delete()
        return redirect('home')
    return redirect('home') 

def update(request,id):
    vehicle = get_object_or_404(Service, id=id)
    data={
        'vehicle':vehicle,
    }

    if request.method == 'POST':
        data=request.POST
        vehicle.vehicle_number=data.get('number')
        vehicle.vehicle_type=data.get('type')
        vehicle.vehicle_model=data.get('model')
        vehicle.vehicle_desc=data.get('desc')
        vehicle.save()
        return redirect('home')
        print(vehicle_type)
    #print(data.vehicle.vehicle_number)



    return render(request,"edit.html",{'vehicle': vehicle})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the desired page after successful login
        else:
            # Handle invalid login credentials
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')