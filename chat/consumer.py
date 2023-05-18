import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from SMBM_APP.models import Chat
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room_name']
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        # print(self.room_group_name)
        chats = Chat.objects.filter(user_id_id=self.room_group_name)
       
        for chat in chats:
            # print(chat.from_user,chat.user_id.username,chat.message,chat.date)
            self.send(json.dumps({
                'from_user': chat.from_user,
                'username': chat.user_id.username,
                'message': chat.message,
                'date':str(chat.date),
            }))
    
    def receive(self,text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        from_user=text_data_json['from_user']

        user=User.objects.get(id=self.room_group_name)
        chat=Chat.objects.create(user_id=user,message=message,from_user=from_user)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':message,
                'from_user':from_user,
                'date':str(chat.date),
            }
        )

       
    def chat_message(self,event):
        message=event['message']
        from_user=event['from_user']
        date=event['date']
        self.send(text_data=json.dumps({
            'message':message,
            'type':'chat',
            'from_user':from_user,
            'date':date,
            
        }))