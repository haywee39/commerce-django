from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.



def registrationPage(request):

    if request.user.is_authenticated:
        return redirect('shop')

    else:

        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'items/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('post')

    else:


        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)


            if user is not None:
                login(request, user)
                return redirect('shop')

            else:
                messages.info(request, 'Username OR Password is incorrect')

        return render(request,'items/login.html')



def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def shop(request):

    
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'items/flowerbay.html',context)



