from msgspec import field

from .sandbox_v2_coin_type import SandboxV2CoinType
from ..common import BaseStruct


class SandboxV2ShopGoodData(BaseStruct):
    goodId: str
    itemId: str
    count: int
    coinType: SandboxV2CoinType
    value: int
    itemPoolId: str | None = field(default=None)
    stock: int | None = field(default=None)
    weight: int | None = field(default=None)
