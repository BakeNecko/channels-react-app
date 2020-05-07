from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from .middleware import TokenAuthMiddleware
from chat.consumers import ChatConsumer


application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter([
            path('chat/', ChatConsumer),
        ])
    ),
})
