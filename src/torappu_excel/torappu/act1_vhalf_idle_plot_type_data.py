from .act1_vhalf_idle_plot_type import Act1VHalfIdlePlotType
from ..common import BaseStruct


class Act1VHalfIdlePlotTypeData(BaseStruct):
    plotType: Act1VHalfIdlePlotType
    typeName: str
    plotSquadLimit: dict[str, list[int]]
