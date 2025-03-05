from .roguelike_activity_basic_data import RoguelikeActivityBasicData
from .roguelike_activity_table import RoguelikeActivityTable
from ..common import BaseStruct


class RoguelikeActivityData(BaseStruct):
    basicDatas: dict[str, RoguelikeActivityBasicData]
    activityTable: RoguelikeActivityTable
