from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
# Create your views here.

def sellerRegister(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        Bs_name = request.POST['bs_name']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        address = request.POST['add']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        password = request.POST['pwd']
        confoirm_pass = request.POST['confirm_pwd']
        name = firstname+lastname

        # if username is already exits
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'email is already exists')
            return redirect('seller')

        else:
            if password != confoirm_pass:
                messages.add_message(request, messages.ERROR, 'password is not match ')
                return redirect('seller')

            User.objects.create_user(first_name=firstname,last_name = lastname,username=email, email=email,password=password).save()
            adminUserInfo(name = name, bs_name=Bs_name, contact=contact_no,address=address,city=city, state=state, zip_code=zip_code,).save()
    else:
        return render(request, 'register.html', {})





def addSellerData(request):
    name = request.POST['name']
    Bs_name= request.POST['bs_name']
    email = request.POST['email']
    contact_no = request.POST['contact_no']
    address = request.POST['add']
    city = request.POST['city']
    state = request.POST['state']
    zip_code = request.POST['zip_code']
    password = request.POST['pwd']
    confoirm_pass = request.POST['confirm_pwd']


    # if username is already exits
    if adminUserInfo.objects.filter(email = email).exists():
        messages.add_message(request, messages.ERROR, 'email is already exists')
        return redirect('sellerRegister')

    else:
        if password!=confoirm_pass:
            messages.add_message(request, messages.ERROR, 'password is not match ')
            return redirect('sellerRegister')

        adminUserInfo.objects.create_user(name = name, bs_name = Bs_name, email= email, contact = contact_no, address = address, city = city, state = state, zip_code = zip_code, password = password ).save()



