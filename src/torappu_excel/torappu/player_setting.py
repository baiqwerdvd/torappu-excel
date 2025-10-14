from pydantic import BaseModel, ConfigDict

from .player_setting_perf import PlayerSettingPerf


class PlayerSetting(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    perf: PlayerSettingPerf
