from pydantic import BaseModel, ConfigDict


class RoguelikeGameShopDialogData(BaseModel):
    class RoguelikeGameShopDialogTypeData(BaseModel):
        class RoguelikeGameShopDialogGroupData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            content: list[str]

        groups: dict[
            str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData.RoguelikeGameShopDialogGroupData"
        ]

    types: dict[str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData"]
