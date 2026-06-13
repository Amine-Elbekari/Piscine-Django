import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, ChatRoom

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope["url_route"]["kwargs"]["room"]
        self.group_name = f"chat_{self.room}"

        await self.channel_layer.group_add(
            self.group_name, self.channel_name
        )
        await self.accept()

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.content',
                'content': f"{self.scope['user'].username} has joined the chat",
                'user': '',
            }
        )

        messages = await self.get_recent_messages(self.room, 3)
        for msg in messages:
            # self.send sends only to the user who just connected
            # unlike group_send that sends to all users in the room
            await self.send(text_data=json.dumps({
                'content': msg.content,
                'user': msg.user.username,
            }))
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.save_message(self.room, self.scope['user'], data['content'])
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.content',
                'content': data['content'],
                'user': self.scope['user'].username,
            }
        )
    
    async def chat_content(self, event):
        await self.send(text_data=json.dumps({
            'content': event['content'],
            'user': event['user'],
        }))

    @database_sync_to_async
    def save_message(self, room_name, user, content):
        room = ChatRoom.objects.get(name=room_name)
        return Chat.objects.create(
            room=room,
            user=user, 
            content=content
        )

    @database_sync_to_async
    def get_recent_messages(self, room_name, limit):
        room = ChatRoom.objects.get(name=room_name)
        return list(
            Chat.objects.filter(room=room)
            .select_related('user')
            .order_by("timestamp")[:limit]
        )