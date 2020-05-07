from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack
from chat.consumers import ChatConsumer


application = ProtocolTypeRouter({
    'websocket': ChatConsumer(
        URLRouter([
            path('chat/', ChatConsumer),
        ])
    ),
})