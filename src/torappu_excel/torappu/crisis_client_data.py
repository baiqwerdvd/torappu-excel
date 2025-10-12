from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class CrisisClientData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonId: str
    startTs: int
    endTs: int
    name: str
    crisisRuneCoinUnlockItem: ItemBundle
    permBgm: str
    medalGroupId: str | None
    bgmHardPoint: int
    permBgmHard: str | None
