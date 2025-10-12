from pydantic import BaseModel, ConfigDict, Field

from .item_bundle import ItemBundle


class RoguelikeTopicBPGrandPrize(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    grandPrizeDisplayId: str
    sortId: int
    displayUnlockYear: int
    displayUnlockMonth: int
    acquireTitle: str
    purchaseTitle: str
    displayName: str
    displayDiscription: str
    bpLevelId: str
    itemBundle: ItemBundle | None = Field(default=None)
    accordingCharId: str | None = Field(default=None)
    accordingSkinId: str | None = Field(default=None)
    detailAnnounceTime: str | None = Field(default=None)
    picIdAftrerUnlock: str | None = Field(default=None)
