# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a message is created in a subscribed text channel"""

from ..core.dispatch import GatewayDispatch
from ..objects import UserMessage


async def message_create_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_message`` event,
        generate a class for the message that has been created.

    :param self:
        The current client.

    :param payload:
        The data received from the message creation event.

    """
    return "on_message", [
        UserMessage.from_dict(
            {"_client": self, "_http": self.http, **payload.data}
        )
    ]


def export():
    return message_create_middleware
