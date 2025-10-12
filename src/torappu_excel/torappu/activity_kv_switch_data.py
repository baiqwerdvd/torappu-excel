from pydantic import BaseModel, ConfigDict

from .kv_switch_info import KVSwitchInfo


class ActivityKVSwitchData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    kvSwitchInfo: dict[str, KVSwitchInfo]
