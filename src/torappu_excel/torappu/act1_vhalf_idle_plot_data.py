from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_plot_combine_type import Act1VHalfIdlePlotCombineType
from .act1_vhalf_idle_plot_type import Act1VHalfIdlePlotType


class Act1VHalfIdlePlotData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class ItemDropData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        itemDropDesc: str

    class PlotCombineData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        combineType: Act1VHalfIdlePlotCombineType
        plots: list["Act1VHalfIdlePlotData.PlotCombineData.CombineItemData"]

        class CombineItemData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            plotId: str
            plotCount: int
