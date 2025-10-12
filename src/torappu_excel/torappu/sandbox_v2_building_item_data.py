from pydantic import BaseModel, ConfigDict


class SandboxV2BuildingItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    itemRarity: int
