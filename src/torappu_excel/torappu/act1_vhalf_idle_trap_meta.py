from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_plot_type import Act1VHalfIdlePlotType
from .half_idle_trap_buildable_type import HalfIdleTrapBuildableType


class Act1VHalfIdleTrapMeta(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    trapType: Act1VHalfIdlePlotType
    buildType: HalfIdleTrapBuildableType
    skillIndex: int
    dropWeight: float
    defaultPlotId: str
