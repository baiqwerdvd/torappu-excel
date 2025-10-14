from pydantic import BaseModel, ConfigDict


class PlayerGoodItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    count: int
