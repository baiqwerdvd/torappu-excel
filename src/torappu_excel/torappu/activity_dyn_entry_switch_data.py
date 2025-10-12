from pydantic import BaseModel, ConfigDict

from .dyn_entry_switch_info import DynEntrySwitchInfo


class ActivityDynEntrySwitchData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    entrySwitchInfo: dict[str, DynEntrySwitchInfo]
    randomEntrySwitchInfo: dict[str, DynEntrySwitchInfo]
