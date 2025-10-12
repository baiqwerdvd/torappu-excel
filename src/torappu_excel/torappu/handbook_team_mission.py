from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class HandbookTeamMission(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sort: int
    powerId: str
    powerName: str
    item: ItemBundle
    favorPoint: int
