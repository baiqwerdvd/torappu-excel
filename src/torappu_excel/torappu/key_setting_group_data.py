from .activity_type import ActivityType
from .key_effect_group import KeyEffectGroup
from .key_setting_group import KeySettingGroup
from .key_setting_item_data import KeySettingItemData
from ..common import BaseStruct


class KeySettingGroupData(BaseStruct):
    groupId: str
    name: str
    funcType: KeySettingGroup
    keyEffectGroup: KeyEffectGroup
    isHidden: bool
    relatedActType: ActivityType
    gameModeTag: str | None
    sortId: int
    startTs: int
    itemList: list[KeySettingItemData]
