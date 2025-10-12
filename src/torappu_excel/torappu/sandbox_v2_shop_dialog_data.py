from pydantic import BaseModel, ConfigDict


class SandboxV2ShopDialogData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonDialogs: dict[str, list[str]]
    afterBuyDialogs: list[str]
    shopEmptyDialogs: list[str]
