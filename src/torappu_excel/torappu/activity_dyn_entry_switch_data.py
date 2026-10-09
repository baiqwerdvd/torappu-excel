from .dyn_entry_animation_info import DynEntryAnimationInfo
from .dyn_entry_switch_info import DynEntrySwitchInfo
from ..common import BaseStruct


class ActivityDynEntrySwitchData(BaseStruct):
    entrySwitchInfo: dict[str, DynEntrySwitchInfo]
    randomEntrySwitchInfo: dict[str, DynEntrySwitchInfo]
    entryAnimationInfo: dict[str, DynEntryAnimationInfo]
