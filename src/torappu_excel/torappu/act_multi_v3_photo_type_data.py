from pydantic import BaseModel, ConfigDict

from .act_multi_v3_photo_slot_data import ActMultiV3PhotoSlotData


class ActMultiV3PhotoTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    photoTypeName: str
    sortId: int
    background: str
    photoDesc: str
    slots: list[ActMultiV3PhotoSlotData]
