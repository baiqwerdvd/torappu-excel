from ..common import BaseStruct


class ArkNewsData(BaseStruct):
    battleItemLevelDataList: "list[ArkNewsData.ArkNewsBuffItemData]"

    class ArkNewsBuffItemData(BaseStruct):
        level: int
        desc: str | None
        templateTrapId: str | None
