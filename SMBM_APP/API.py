from rest_framework import generics
from .models import Slot,Chat
from .serializers import SlotSerializer,ChatSerializer,MessageSerializer
from django.contrib.auth.models import User


class SlotList(generics.ListCreateAPIView):
    queryset = Slot.objects.filter(avalible=True)
    serializer_class = SlotSerializer

class ChatList (generics.ListCreateAPIView):
        lookup_url_kwarg = 'q'
        
        queryset = User.objects.filter(is_staff=False)
        serializer_class = ChatSerializer

        def get_queryset(self):
            chat_type = self.kwargs['q']
            return User.objects.filter(is_staff=False,username__icontains=chat_type)

class MessageList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    
    serializer_class = MessageSerializer

    def get_queryset(self):
            
     list_chat = []
     users=User.objects.filter(is_staff=False)
     for chat in users:
        chats2=Chat.objects.filter(user_id=chat)
        latest_chat = chats2.latest('id')
        latest_chat.date=str(latest_chat.date)
        list_chat.append(latest_chat)

     return list_chat   
    
class SingleuserList (generics.ListCreateAPIView):
        lookup_url_kwarg = 'q'
        
        queryset = User.objects.filter(is_staff=False)
        serializer_class = ChatSerializer

        def get_queryset(self):
           chat_type = self.kwargs['q']
           print(chat_type,'chattype')
           return User.objects.filter(id=chat_type)

