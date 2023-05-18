from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback,Chat,Point,Rewards
from django.contrib.auth.models import User

@login_required(login_url='login')
def redeem_rewards(request):
    point=Point.objects.get(user_id_id=request.user.id)
    # point.current_point += 200
    # point.save()
    print(type(point.current_point))

    if request.method == "POST":
        reward=request.POST['reward']
        point_used = int(request.POST['point'])

        Rewards.objects.create(rewards=reward,status=True,user_id_id=request.user.id)
        
        point.current_point-=point_used
        point.used_point+=point_used
        point.save()

    return render(request,'redeem_chat_feedback/redemreward.html',{'point':point})

@login_required(login_url='login')
def redeem_history(request):
    
    return render(request,'redeem_chat_feedback/redeemhistory.html')




@login_required(login_url='login')
def feedback(request):
    context={'form':FeedbackForm({'user_id': request.user.id})}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # my_instance.save()
            context['message']='SUCCESSFUL'


    return render(request,'redeem_chat_feedback/feedback.html',context)

@login_required(login_url='login')
def retri_feedback(request):
    context = {'feedback_info':Feedback.objects.all()}
    return render(request,'redeem_chat_feedback/retrieveFeedback.html',context)

def feedback_delete(request,id):
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('retri_feedback')


@login_required(login_url='login')
def chat(request):
    return render(request,'redeem_chat_feedback/chat.html')


@login_required(login_url='login')
def chat_info(request):
    # list_chat = []
    # chats=User.objects.filter(is_staff=False)
    # for user in chats:
    #   chats2=Chat.objects.filter(user_id_id=user.id)
    #   latest_chat = chats2.latest('id')
    #   latest_chat.date=str(latest_chat.date)
    #   list_chat.append(latest_chat)
    #   print(list_chat)
    return render(request,'redeem_chat_feedback/chatInfo.html')

@login_required(login_url='login')
def chat_delete(request,id):
    print(id,'id')
    chats=Chat.objects.filter(user_id_id=id)
    chats.delete()
    return render(request,'redeem_chat_feedback/chat.html')