from .act1_vhalf_idle_plot_combine_type import Act1VHalfIdlePlotCombineType
from .act1_vhalf_idle_plot_type import Act1VHalfIdlePlotType
from ..common import BaseStruct


class Act1VHalfIdlePlotData(BaseStruct):
    plotId: str
    plotName: str
    plotType: Act1VHalfIdlePlotType
    trapId: str
    initUnlock: bool
    rarity: int
    sortId: int
    isBasePlot: bool
    iconId: str
    funcDesc: str
    flavorDesc: str | None
    enemyIds: list[str]
    enemyDesc: str | None
    itemIdShown: str | None
    itemDropData: list["Act1VHalfIdlePlotData.ItemDropData"]
    prevCombineData: "Act1VHalfIdlePlotData.PlotCombineData | None"
    derivedPlots: list[str]

    class ItemDropData(BaseStruct):
        itemId: str
        itemDropDesc: str

    class PlotCombineData(BaseStruct):
        combineType: Act1VHalfIdlePlotCombineType
        plots: list["Act1VHalfIdlePlotData.PlotCombineData.CombineItemData"]

        class CombineItemData(BaseStruct):
            plotId: str
            plotCount: int
