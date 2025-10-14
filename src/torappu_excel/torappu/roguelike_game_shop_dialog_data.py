from pydantic import BaseModel, ConfigDict


class RoguelikeGameShopDialogData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    types: dict[str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData"]

    class RoguelikeGameShopDialogTypeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        class RoguelikeGameShopDialogGroupData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            content: list[str]

        groups: dict[
            str, "RoguelikeGameShopDialogData.RoguelikeGameShopDialogTypeData.RoguelikeGameShopDialogGroupData"
        ]
