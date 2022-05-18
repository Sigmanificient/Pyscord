# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild role was updated."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildRoleUpdateEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_role_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
):
    """|coro|

    Middleware for the ``on_guild_role_update`` event.

    Parameters
    ----------
    payload : :class:`~pincer.core.gateway.GatewayDispatch`
        The data received from the guild role update event.
    gateway : :class:`~pincer.core.gateway.Gateway`
        The gateway for the current shard.

    Returns
    -------
    Tuple[:class:`str`, :class:`~pincer.objects.events.guild.GuildRoleUpdateEvent`]
        ``on_guild_role_update`` and a ``GuildRoleUpdateEvent``
    """

    event = GuildRoleUpdateEvent.from_dict(payload.data)
    if guild := self.guilds.get(event.guild_id):
        guild.roles = [
            role if role.id != event.role.id else event.role
            for role in guild.roles
        ]

    return ("on_guild_role_update", event)


def export() -> Coro:
    return guild_role_update_middleware
