from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth.decorators import login_required
from .models import Slot,Booking,Rewards,Point
from .forms import SlotForm,BookingForm
from django.contrib.auth.models import User


@login_required(login_url='login')
def book_now(request): 

    return render(request,'booking/bookNow.html')

@login_required(login_url='login')
def make_booking(request):
    if Slot.objects.all().exists():
        return render(request,'booking/makebooking2.html',{'slot':Slot.objects.all()})
        
    return render(request,'booking/makebooking.html')



@login_required(login_url='login')
def booking_ticket(request):
    
    type=request.GET['type']
    date=request.GET['date']
    time=request.GET['slot']
    slot=Slot.objects.get(date=date)
    # try:
    #     customer_id = request.GET['customer_id']
    #     customer= User.objects.get(id=customer_id)
    # except: 
    #     customer = request.user.id
    #   point=Point.objects.get(user_id_id=request.user.id)
    try:
        customer_id=request.GET['customer_id']

        form=BookingForm({'user_id': User.objects.get(id=customer_id),'date':date,'time':time,'type':type,'slot_id':slot},request= User.objects.get(id=customer_id))
    except :
        form=BookingForm({'user_id': request.user.id,'date':date,'time':time,'type':type,'slot_id':slot},request=request)
        point=Point.objects.get(user_id_id=request.user.id)
    # form=BookingForm({'user_id': customer,'date':date,'time':time,'type':type,'slot_id':slot},request=request)
    
  
    
    if request.method == 'POST':
        form = BookingForm(request.POST,request=request)
        if form.is_valid():
            form_1=form.cleaned_data['rewards_id']
            form_1.delete()
            total =form.cleaned_data['adult']+form.cleaned_data['concession']+form.cleaned_data['child']
            if type=='Guided Tour':
                total *=3 
            else:
                total *=8
            point.current_point += total
            point.save()
            form.save()
            latest_id = Booking.objects.latest('id').id
            
            return render(request,'booking/detail.html',{'mydata':Booking.objects.get(id=latest_id)})
        else:
            print(form.errors)
    
    context={'type':type,'date':date,'time':time,'form':form,'slot':slot}
          
    return render(request,'booking/ticket.html',context)

@login_required(login_url='login')
def booking_detail(request):
    
    Booking.objects.get()
    
    return render(request,'booking/detail.html')

@login_required(login_url='login')


@login_required(login_url='login')
def customer_booking(request):
    user_id = request.user.id
    if Booking.objects.filter(user_id_id=user_id).exists():
        context ={'data':Booking.objects.filter(user_id_id=user_id)} 
        print(context)
        print('have') 
    else:
       print('notHave')
       return render(request,'booking/customerBookings.html')
    
    return render(request,'booking/managebooking.html',context)

@login_required(login_url='login')
def customer_booking2(request):
    
    context ={'customer':User.objects.filter(is_staff=False) }
   
    return render(request,'booking/customerBookings2.html',context)

def managebooking(request):
  
    context = {'data':Booking.objects.all()}

    return render(request,'booking/managebooking.html',context)

@login_required(login_url='login')
def view_slot(request):
    context={'slotList':Slot.objects.all()}
    return render(request,'booking/view_slot.html',context)

@login_required(login_url='login')
def create_slot(request):
    context = {'form':SlotForm()}
    if request.method == 'POST':
        form=SlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_slot')
        else:
            return render(request,'booking/create_slot.html',{'form':form})
    return render(request,'booking/create_slot.html',context)

def clear_allslot(request):
    clear_slot=Slot.objects.all()
    clear_slot.delete()
    return redirect('view_slot')

def delete_slot(request,id):

     slot_id=Slot.objects.get(id=id)
     slot_id.delete()
     return redirect('view_slot')

def update_slot(request,id):
    slot=Slot.objects.get(id=id)
    context = {'form':SlotForm(instance=slot)}
    if request.method == 'POST':
        form = SlotForm(request.POST,instance=slot)
        form.save()
        return redirect ('view_slot')

    return render(request,'booking/update_slot.html',context)

def avalible(request,id):
    slot=Slot.objects.get(id=id)
    slot.avalible=True
    slot.save()
    return redirect ('view_slot')   

def unavalible(requestid,id):
    slot=Slot.objects.get(id=id)
    slot.avalible=False
    slot.save()
    return redirect ('view_slot') 
