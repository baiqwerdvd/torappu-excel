from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeNodeUpgradeModuleData(BaseStruct):
    class RoguelikeNodeUpgradeData(BaseStruct):
        class RoguelikePermNodeUpgradeItemData(BaseStruct):
            upgradeId: str
            nodeType: RoguelikeEventType
            nodeLevel: int
            costItemId: str
            costItemCount: int
            desc: str
            nodeName: str

        class RoguelikeTempNodeUpgradeItemData(BaseStruct):
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
