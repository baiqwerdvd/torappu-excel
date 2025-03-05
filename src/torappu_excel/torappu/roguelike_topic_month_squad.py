from .item_bundle import ItemBundle
from .roguelike_topic_month_squad_team_char import RoguelikeTopicMonthSquadTeamChar
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicMonthSquad(BaseStruct):
    id_: str = field(name="id")
    teamName: str
    teamSubName: str | None
    teamFlavorDesc: str | None
    teamDes: str
    teamColor: str
    teamMonth: str
    teamYear: str
    teamIndex: str | None
    teamChars: list[RoguelikeTopicMonthSquadTeamChar | str]
    zoneId: str | None
    chatId: str
    tokenRewardNum: int
    items: list[ItemBundle]
    startTime: int
    endTime: int
    taskDes: str | None
