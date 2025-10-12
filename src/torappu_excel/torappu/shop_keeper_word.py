from pydantic import BaseModel, ConfigDict


class ShopKeeperWord(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    text: str
