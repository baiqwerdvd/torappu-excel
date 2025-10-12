from pydantic import BaseModel, ConfigDict


class ActMultiV3PhotoSlotData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    slotPosX: float
    slotPosY: float
    slotRotZ: int
    slotScale: float
    slotAnimName: str
