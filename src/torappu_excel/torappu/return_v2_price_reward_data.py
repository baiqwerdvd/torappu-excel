from pydantic import BaseModel, ConfigDict

from .return_v2_item_data import ReturnV2ItemData


class ReturnV2PriceRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    contentId: str
    sortId: int
    pointRequire: int
    desc: str
    iconId: str
    topIconId: str
    rewardList: list[ReturnV2ItemData]
