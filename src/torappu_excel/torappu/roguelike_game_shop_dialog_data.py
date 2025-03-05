from ..common import BaseStruct


class RoguelikeGameShopDialogData(BaseStruct):
    class RoguelikeGameShopDialogTypeData(BaseStruct):
        class RoguelikeGameShopDialogGroupData(BaseStruct):
            content: list[str]

        groups: dict[
            str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData.RoguelikeGameShopDialogGroupData"
        ]

    types: dict[str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData"]
