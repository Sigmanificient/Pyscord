# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from typing import overload, TYPE_CHECKING
from enum import IntEnum
from dataclasses import dataclass, field

from ...utils.types import MISSING
from ...utils.api_object import APIObject

if TYPE_CHECKING:
    from typing import Dict, List, Optional

    from .role import Role
    from .channel import Channel
    from ...client import Client
    from .member import GuildMember
    from .stage import StageInstance
    from ..message.emoji import Emoji
    from .features import GuildFeatures
    from ..message.sticker import Sticker
    from ...utils.types import APINullable
    from ...utils.snowflake import Snowflake
    from ...utils.timestamp import Timestamp
    from ..user.voice_state import VoiceState
    from .welcome_screen import WelcomeScreen
    from ...exceptions import UnavailableGuildError
    from ..events.presence import PresenceUpdateEvent


class PremiumTier(IntEnum):
    """Represents the boost tier of a guild.

    Attributes
    ----------
    NONE:
        Guild has not unlocked any Server Boost perks.
    TIER_1:
        Guild has unlocked Server Boost level 1 perks.
    TIER_2:
        Guild has unlocked Server Boost level 2 perks.
    TIER_3:
        Guild has unlocked Server Boost level 3 perks.
    """
    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class GuildNSFWLevel(IntEnum):
    """Represents the NSFW level of a guild.

    Attributes
    ----------
    DEFAULT:
        Default NSFW level.
    EXPLICIT:
        Explicit NSFW level.
    SAFE:
        SAFE NSFW level.
    AGE_RESTRICTED:
        Age restricted NSFW level.
    """
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class ExplicitContentFilterLevel(IntEnum):
    """Represents the filter content level of a guild.

    Attributes
    ----------
    DISABLED:
        Media content will not be scanned.
    MEMBERS_WITHOUT_ROLES:
        Media content sent by members without roles will be scanned.
    ALL_MEMBERS:
        Media content sent by all members will be scanned.
    """
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class MFALevel(IntEnum):
    """Represents the multi factor authentication level of a guild.

    Attributes
    ----------
    NONE:
        Guild has no MFA/2FA requirement for moderation actions.
    ELEVATED:
        Guild has a 2FA requirement for moderation actions
    """
    NONE = 0
    ELEVATED = 1


class VerificationLevel(IntEnum):
    """Represents the verification level of a guild.

    Attributes
    ----------
    NONE:
        Unrestricted.
    LOW:
        Must have verified email on account.
    MEDIUM:
        Must be registered on Discord for longer than 5 minutes.
    HIGH:
        Must be a member of the server for longer than 10 minutes.
    VERY_HIGH:
        Must have a verified phone number.
    """
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class DefaultMessageNotificationLevel(IntEnum):
    """Represents the default message notification level of a guild.

    Attributes
    ----------
    ALL_MESSAGES:
        Members will receive notifications for all messages by default.
    ONLY_MENTIONS:
        Members will receive notifications only for messages that @mention them by default.
    """  # noqa: E501
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class SystemChannelFlags(IntEnum):
    """Represents the system channel flags of a guild.

    Attributes
    ----------
    SUPPRESS_JOIN_NOTIFICATIONS:
        Suppress member join notifications.
    SUPPRESS_PREMIUM_SUBSCRIPTIONS:
        Suppress server boost notifications.
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS:
        Suppress server setup tips.
    """
    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2


@dataclass
class Guild(APIObject):
    """Represents a Discord guild/server in which your client resides.

    Attributes
    ----------
    afk_channel_id: Optional[:class:`~pincer.utils.snowflake.Snowflake`]
        Id of afk channel
    afk_timeout: :class:`int`
        Afk timeout in seconds
    application_id: Optional[:class:`~pincer.utils.snowflake.Snowflake`]
        Application id of the guild creator if it is bot-created
    banner: Optional[:class:`str`]
        Banner hash
    default_message_notifications: :class:`~pincer.objects.guild.guild.DefaultMessageNotificationLevel`
        Default message notifications level
    description: Optional[:class:`str`]
        The description of a Community guild
    discovery_splash: Optional[:class:`str`]
        Discovery splash hash;
        only present for guilds with the "DISCOVERABLE" feature
    emojis: List[:class:`~pincer.objects.message.emoji.Emoji`]
        Custom guild emojis
    explicit_content_filter: :class:`~pincer.objects.guild.guild.ExplicitContentFilterLevel`
        Explicit content filter level
    features: List[:class:`~pincer.objects.guild.features.GuildFeatures`]
        Enabled guild features
    id: :class:`~pincer.utils.snowflake.Snowflake`
        Guild id
    icon: Optional[:class:`str`]
        Icon hash
    mfa_level: :class:`~pincer.objects.guild.guild.MFALevel`
        Required MFA level for the guild
    name: :class:`str`
        Guild name (2-100 characters, excluding trailing and leading
        whitespace)
    nsfw_level: :class:`~pincer.objects.guild.guild.NSFWLevel`
        Guild NSFW level
    owner_id: :class:`~pincer.utils.snowflake.Snowflake`
        Id of owner
    preferred_locale: :class:`str`
        The preferred locale of a Community guild;
        used in server discovery and notices from Discord;
        defaults to "en-US"
    premium_tier: :class:`~pincer.objects.guild.guild.PremiumTier`
        Premium tier (Server Boost level)
    public_updates_channel_id: Optional[:class:`~pincer.utils.snowflake.Snowflake`]
        The id of the channel where admins
        and moderators of Community guilds receive notices from Discord
    roles: List[:class:`~pincer.objects.guild.role.Role`]
        Roles in the guild
    rules_channel_id: Optional[:class:`~pincer.utils.snowflake.Snowflake`]
        The id of the channel where Community guilds can display rules
        and/or guidelines
    splash: Optional[:class:`str`]
        Splash hash
    system_channel_flags: :class:`~pincer.objects.guild.guild.SystemChannelFlags`
        System channel flags
    system_channel_id: Optional[:class:`~pincer.utils.snowflake.Snowflake`]
        The id of the channel where guild notices
        such as welcome messages and boost events are posted
    vanity_url_code: Optional[:class:`str`]
        The vanity url code for the guild
    verification_level: :class:`~pincer.objects.guild.guild.VerificationLevel`
        Verification level required for the guild
    approximate_member_count: APINullable[:class:`int`]
        Approximate number of members in this guild, returned from the
        `GET /guilds/<id>` endpoint when with_counts is true
    approximate_presence_count: APINullable[:class:`int`]
        Approximate number of non-offline members in this guild,
        returned from the `GET /guilds/<id>`
        endpoint when with_counts is true
    channels: APINullable[List[:class:`~pincer.objects.guild.chanenl.Channel`]]
        Channels in the guild
    icon_hash: APINullable[Optional[:class:`str`]]
        Icon hash, returned when in the template object
    joined_at: APINullable[:class:`~pincer.utils.timestamp.Timestamp`]
        When this guild was joined at
    large: APINullable[:class:`bool`]
        True if this is considered a large guild
    max_members: APINullable[:class:`int`]
        The maximum number of members for the guild
    max_presences: APINullable[Optional[:class:`int`]]
        The maximum number of presences for the guild
        (null is always returned, apart from the largest of guilds)
    max_video_channel_users: APINullable[:class:`int`]
        The maximum amount of users in a video channel
    members: APINullable[List[:class:`~pincer.objects.guild.member.GuildMember`]]
        Users in the guild
    member_count: APINullable[:class:`bool`]
        Total number of members in this guild
    nsfw: APINullable[:class:`bool`]
        Boolean if the server is NSFW
    owner: APINullable[:class:`bool`]
        True if the user is the owner of the guild
    permissions: APINullable[:class:`str`]
        Total permissions for the user in the guild
        (excludes overwrites)
    premium_subscription_count: APINullable[:class:`int`]
        The number of boosts this guild currently has
    presences: APINullable[List[:class:`~pincer.objects.events.presence.PresenceUpdateEvent`]]
        Presences of the members in the guild,
        will only include non-offline members if the size is greater
        than large threshold
    stage_instances: APINullable[List[:class:`~pincer.objects.guild.stage.StageInstance`]]
        Stage instances in the guild
    stickers: Optional[List[:class:`~pincer.objects.message.sticker.Sticker`]]
        Custom guild stickers
    region: APINullable[Optional[:class:`str`]]
        Voice region id for the guild (deprecated)
    threads: APINullable[List[:class:`~pincer.objects.guild.channel.Channel`]]
        All active threads in the guild that current user
        has permission to view
    unavailable: APINullable[:class:`bool`]
        True if this guild is unavailable due to an outage
    voice_states: APINullable[List[:class:`~pincer.objects.user.voice_state.VoiceState`]]
        States of members currently in voice channels;
        lacks the guild_id key
    widget_enabled: APINullable[:class:`bool`]
        True if the server widget is enabled
    widget_channel_id: APINullable[Optional[:class:`~pincer.utils.snowflake.Snowflake`]]
        The channel id that the widget will generate an invite to,
        or null if set to no invite
    welcome_screen: APINullable[:class:`~pincer.objects.guild.welcome_screen.WelcomeScreen`]
        The welcome screen of a Community guild, shown to new members,
        returned in an Invite's guild object
    """
    afk_channel_id: Optional[Snowflake]
    afk_timeout: int
    application_id: Optional[Snowflake]
    embedded_activities: Optional[List]
    banner: Optional[str]
    default_message_notifications: DefaultMessageNotificationLevel
    description: Optional[str]
    discovery_splash: Optional[str]
    emojis: List[Emoji]
    explicit_content_filter: ExplicitContentFilterLevel
    features: List[GuildFeatures]
    id: Snowflake
    icon: Optional[str]
    mfa_level: MFALevel
    name: str
    nsfw_level: GuildNSFWLevel
    owner_id: Snowflake
    preferred_locale: str
    premium_tier: PremiumTier
    public_updates_channel_id: Optional[Snowflake]
    roles: List[Role]
    rules_channel_id: Optional[Snowflake]
    splash: Optional[str]
    system_channel_flags: SystemChannelFlags
    system_channel_id: Optional[Snowflake]
    vanity_url_code: Optional[str]
    verification_level: VerificationLevel
    guild_scheduled_events: Optional[List]
    lazy: Optional[bool]
    premium_progress_bar_enabled: Optional[bool]
    guild_hashes: Optional[Dict]

    application_command_counts: APINullable[Dict] = MISSING
    application_command_count: APINullable[int] = MISSING
    approximate_member_count: APINullable[int] = MISSING
    approximate_presence_count: APINullable[int] = MISSING
    channels: APINullable[List[Channel]] = field(default_factory=list)
    # TODO: Add type when type is known
    hub_type: APINullable[...] = MISSING
    icon_hash: APINullable[Optional[str]] = MISSING
    joined_at: APINullable[Timestamp] = MISSING
    large: APINullable[bool] = MISSING
    max_members: APINullable[int] = MISSING
    max_presences: APINullable[Optional[int]] = MISSING
    max_video_channel_users: APINullable[int] = MISSING
    members: APINullable[List[GuildMember]] = MISSING
    member_count: APINullable[bool] = MISSING
    nsfw: APINullable[bool] = MISSING
    # Note: This is missing from discord's docs but in the api
    owner: APINullable[bool] = MISSING
    permissions: APINullable[str] = MISSING
    premium_subscription_count: APINullable[int] = MISSING
    presences: APINullable[List[PresenceUpdateEvent]] = MISSING
    stage_instances: APINullable[List[StageInstance]] = MISSING
    stickers: APINullable[List[Sticker]] = MISSING
    region: APINullable[Optional[str]] = MISSING
    threads: APINullable[List[Channel]] = MISSING
    # Guilds are considered available unless otherwise specified
    unavailable: APINullable[bool] = False
    voice_states: APINullable[List[VoiceState]] = MISSING
    widget_enabled: APINullable[bool] = MISSING
    widget_channel_id: APINullable[Optional[Snowflake]] = MISSING
    welcome_screen: APINullable[WelcomeScreen] = MISSING

    @classmethod
    async def from_id(cls, client: Client, _id: int) -> Guild:
        data = await client.http.get(f"/guilds/{_id}")
        channel_data = await client.http.get(f"/guilds/{_id}/channels")

        channels: List[Channel] = [
            Channel.from_dict({**i, "_client": client, "_http": client.http})
            for i in (channel_data or [])
        ]

        data.update(
            {
                "_client": client,
                "_http": client.http,
                "channels": channels
            }
        )

        # Once below is fixed. Change this to Guild.from_dict
        return Guild(**data)

    async def get_member(self, _id: int) -> GuildMember:
        """|coro|

        Fetches a GuildMember from its identifier

        Parameters
        ----------
        _id:
            The id of the guild member which should be fetched from the Discord
            gateway.

        Returns
        -------
        :class:`~pincer.objects.guild.member.GuildMember`
            A GuildMember object.
        """
        return await GuildMember.from_id(self._client, self.id, _id)

    @overload
    async def modify_member(
            self, *,
            _id: int,
            nick: Optional[str] = None,
            roles: Optional[List[Snowflake]] = None,
            mute: Optional[bool] = None,
            deaf: Optional[bool] = None,
            channel_id: Optional[Snowflake] = None
    ) -> GuildMember:
        """|coro|

        Modifies a member in the guild from its identifier and based on the
        keyword arguments provided.

        Parameters
        ----------
        _id : int
            Id of the member to modify
        nick : Optional[:class:`str`]
            New nickname for the member |default| :data:`None`
        roles : Optional[List[:class:`~pincer.utils.snowflake.Snowflake]]
            New roles for the member |default| :data:`None`
        mute : Optional[:class:`bool`]
            Whether the member is muted |default| :data:`None`
        deaf : Optional[:class:`bool`]
            Whether the member is defaened |default| :data:`None`
        channel_id : Optional[:class:`~pincer.utils.snowflake.Snowflake]
            Voice channel id to move to |default| :data:`None`

        Returns
        -------
        :class:`~pincer.objects.guild.member.GuildMember`
            The new member object.
        """
        ...

    async def modify_member(self, _id: int, **kwargs) -> GuildMember:
        data = await self._http.patch(f"guilds/{self.id}/members/{_id}", kwargs)
        return GuildMember.from_dict(
            {**data, "_client": self._client, "_http": self._http}
        )

    @classmethod
    def from_dict(cls, data) -> Guild:
        if data.get("unavailable", False):
            raise UnavailableGuildError(
                f"Guild \"{data['id']}\" is unavailable due"
                " to a discord outage."
            )

        return super().from_dict(data)
