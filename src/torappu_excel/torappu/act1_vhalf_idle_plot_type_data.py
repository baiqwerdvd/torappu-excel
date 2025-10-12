from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_plot_type import Act1VHalfIdlePlotType


class Act1VHalfIdlePlotTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    plotType: Act1VHalfIdlePlotType
    typeName: str
    plotSquadLimit: dict[str, list[int]]
