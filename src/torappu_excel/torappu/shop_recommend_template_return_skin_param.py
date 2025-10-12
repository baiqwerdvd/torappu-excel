from pydantic import BaseModel, ConfigDict


class ShopRecommendTemplateReturnSkinParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showStartTs: int
    showEndTs: int
