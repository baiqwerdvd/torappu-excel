from pydantic import BaseModel, ConfigDict

from .roguelike_event_type import RoguelikeEventType


class RoguelikeNodeUpgradeModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeUpgradeDataMap: dict[str, "RoguelikeNodeUpgradeModuleData.RoguelikeNodeUpgradeData"]

    class RoguelikeNodeUpgradeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeType: RoguelikeEventType
        sortId: int
        permItemList: list["RoguelikeNodeUpgradeModuleData.RoguelikeNodeUpgradeData.RoguelikePermNodeUpgradeItemData"]
        tempItemList: list["RoguelikeNodeUpgradeModuleData.RoguelikeNodeUpgradeData.RoguelikeTempNodeUpgradeItemData"]

        class RoguelikePermNodeUpgradeItemData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            upgradeId: str
            nodeType: RoguelikeEventType
            nodeLevel: int
            costItemId: str
            costItemCount: int
            desc: str
            nodeName: str

        class RoguelikeTempNodeUpgradeItemData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            upgradeId: str
            nodeType: RoguelikeEventType
            sortId: int
            costItemId: str
            costItemCount: int
            desc: str
