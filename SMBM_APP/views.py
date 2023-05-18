from django.shortcuts import HttpResponse,render,redirect
from .forms import CustumerRegForm,StuffRegForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Point

# Create your views here.
def home(request):
    return render(request,'index.html')


def customer_resgister(request):
    context={'form':CustumerRegForm()}
    if request.method == "POST":
        form=CustumerRegForm(request.POST)
        if form.is_valid():
            created_user=form.save()
            Point.objects.create(current_point=2,used_point=0, user_id=created_user  ).save()
            # point=Point(current_point=2,user_id=created_user,used_point=0)
            # point.save()
            return render(request,'users/login.html')
        else:
            print(form.errors)
            return render(request, 'users/customerRegisteration.html',{'form':form})
   
    return render(request,'users/customerRegisteration.html',context)


def staff_resgister(request):
    context={'form':StuffRegForm()}
    if request.method == "POST":
        form=StuffRegForm(request.POST)
        if form.is_valid():
            created_user=form.save()
            Point.objects.create(current_point=2,used_point=0, user_id=created_user  )
            return render(request,'users/login.html')
        else:
            return render(request, 'users/staffRegistration.html',{'form':form})
    return render(request,'users/staffRegistration.html',context)

def login_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)    
            return redirect('home')
        else:
            context={'error':'wrong Login Password or UserName'}
            return render(request,'users/login.html',context)
       
    return render(request,'users/login.html')

@login_required(login_url='login')
def after_login(request):

    return render(request,'secondindex.html')

@login_required(login_url='login')
def profile(request):
    
    return render(request,'users/profile.html')

@login_required(login_url='login')
def staff_home(request):
    return render(request,'staff_index.html')

@login_required(login_url='login_page')
def manage_cus_account(request):
    customers = User.objects.filter(is_staff=False)
    
    return render(request,'users/customersManage.html',{'usersList':customers})

@login_required(login_url='login')
def create_cus_acc(request):
    context = { 'form':CustumerRegForm() }
    if request.method == 'POST':
        form = CustumerRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manageCusAcc')
        else:
             return render(request,'users/customers_create.html',{'form':form})
    return render(request,'users/customers_create.html',context)

@login_required(login_url='login')
def staff_manage_acc(request):
    staff = User.objects.filter(is_staff=True)
    
    return render(request,'users/staffmanageAcc.html',{'staffList':staff})


@login_required(login_url='login')
def staff_create_acc(request):
    context = { 'form':StuffRegForm() }
    if request.method == 'POST':
        form = StuffRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_manage_acc')
        else:
             return render(request,'users/staffcreateAcc.html',{'form':form})
    
    return render(request,'users/staffcreateAcc.html',context)

@login_required(login_url='login')
def search_acc(request):
    if request.method == 'POST':
        searchBar=request.POST['searchBar']
        users=User.objects.filter(username__icontains=searchBar)
        context = {'usersList':users}
        return render(request,'users/searchAccount.html',context)
      
    return render(request,'users/searchAccount.html')

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('home')



