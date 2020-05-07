import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

from channels.testing import WebsocketCommunicator
import pytest

from backend.routing import application
from chat.utils import create_user

TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
class TestWebSocket:
    async def test_can_only_login_user_connect_to_server(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        _, access = await create_user(
            'test.user@example.com', 'pAssw0rd'
        )
        communicator = WebsocketCommunicator(
            application=application,
            path=f'/chat/?token={access}'
        )
        connected, _ = await communicator.connect()
        assert connected is True
        await communicator.disconnect()
