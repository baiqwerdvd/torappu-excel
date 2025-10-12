from pydantic import BaseModel, ConfigDict


class UniEquipTypeInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    uniEquipTypeName: str
    sortId: int
    isSpecial: bool
    isInitial: bool
