from pydantic import BaseModel, ConfigDict


class ChooseShopRelation(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    optionList: list[str]
