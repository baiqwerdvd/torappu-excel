from pydantic import BaseModel, ConfigDict

from .sandbox_v2_coin_type import SandboxV2CoinType


class SandboxV2ShopGoodData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    itemId: str
    count: int
    coinType: SandboxV2CoinType
    value: int
