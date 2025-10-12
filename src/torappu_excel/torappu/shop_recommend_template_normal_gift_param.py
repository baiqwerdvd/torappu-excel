from pydantic import BaseModel, ConfigDict


class ShopRecommendTemplateNormalGiftParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showStartTs: int
    showEndTs: int
    goodId: str
    giftPackageName: str
    price: int
    logoId: str
    color: str
    haveMark: bool
    availCount: int = 0
