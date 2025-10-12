from pydantic import BaseModel, ConfigDict

from .roguelike_event_type import RoguelikeEventType


class RoguelikeNodeUpgradeModuleData(BaseModel):
    class RoguelikeNodeUpgradeData(BaseModel):
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

        nodeType: RoguelikeEventType
        sortId: int
        permItemList: list["RoguelikeNodeUpgradeModuleData.RoguelikeNodeUpgradeData.RoguelikePermNodeUpgradeItemData"]
        tempItemList: list["RoguelikeNodeUpgradeModuleData.RoguelikeNodeUpgradeData.RoguelikeTempNodeUpgradeItemData"]

    nodeUpgradeDataMap: dict[str, "RoguelikeNodeUpgradeModuleData.RoguelikeNodeUpgradeData"]
