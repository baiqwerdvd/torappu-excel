from pydantic import BaseModel, ConfigDict


class ShopRecommendTemplateNormalFurnParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showStartTs: int
    showEndTs: int
    furnPackId: str
    isNew: bool
    isPackSell: bool
    count: int
    colorBack: str
    colorText: str
    actId: str | None
