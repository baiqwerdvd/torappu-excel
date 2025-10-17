from ..common import BaseStruct


class RoguelikeGameShopDialogData(BaseStruct):
    types: dict[str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData"]

    class RoguelikeGameShopDialogTypeData(BaseStruct):
        class RoguelikeGameShopDialogGroupData(BaseStruct):
            content: list[str]

        groups: dict[
            str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData.RoguelikeGameShopDialogGroupData"
        ]
