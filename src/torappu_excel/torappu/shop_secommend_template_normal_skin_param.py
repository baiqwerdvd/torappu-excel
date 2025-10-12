from pydantic import BaseModel, ConfigDict


class ShopRecommendTemplateNormalSkinParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showStartTs: int
    showEndTs: int
    skinIds: list[str]
    skinGroupName: str
    brandIconId: str
    colorBack: str
    colorText: str
    text: str
