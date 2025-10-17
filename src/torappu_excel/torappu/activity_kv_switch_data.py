from .kv_switch_info import KVSwitchInfo
from ..common import BaseStruct


class ActivityKVSwitchData(BaseStruct):
    kvSwitchInfo: dict[str, KVSwitchInfo]
