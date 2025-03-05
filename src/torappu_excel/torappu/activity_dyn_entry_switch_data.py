from .dyn_entry_switch_info import DynEntrySwitchInfo
from ..common import BaseStruct


class ActivityDynEntrySwitchData(BaseStruct):
    entrySwitchInfo: dict[str, DynEntrySwitchInfo]
