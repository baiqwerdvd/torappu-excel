from pydantic import BaseModel, ConfigDict

from .act_17side_data import Act17sideData
from .act_20side_data import Act20SideData
from .act_21side_data import Act21SideData
from .act_25side_data import Act25SideData


class ActivityCustomData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    TYPE_ACT17SIDE: dict[str, Act17sideData]
    TYPE_ACT25SIDE: dict[str, "ActivityCustomData.Act25sideCustomData"]
    TYPE_ACT20SIDE: dict[str, Act20SideData]
    TYPE_ACT21SIDE: dict[str, Act21SideData]

    class Act25sideCustomData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        battlePerformanceData: dict[str, Act25SideData.BattlePerformanceData]
