from .act1_vhalf_idle_plot_type import Act1VHalfIdlePlotType
from .half_idle_trap_buildable_type import HalfIdleTrapBuildableType
from ..common import BaseStruct


class Act1VHalfIdleTrapMeta(BaseStruct):
    trapType: Act1VHalfIdlePlotType
    buildType: HalfIdleTrapBuildableType
    skillIndex: int
    dropWeight: float
    defaultPlotId: str
