from .key_item import KeyItem
from .key_setting_group_data import KeySettingGroupData
from .pckey_const_data import PCKeyConstData
from ..common import BaseStruct


class PCKeyData(BaseStruct):
    keyList: dict[str, KeyItem]
    keySettingData: dict[str, KeySettingGroupData]
    constData: PCKeyConstData
