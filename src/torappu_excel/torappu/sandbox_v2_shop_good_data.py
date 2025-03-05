from .sandbox_v2_coin_type import SandboxV2CoinType
from ..common import BaseStruct


class SandboxV2ShopGoodData(BaseStruct):
    goodId: str
    itemId: str
    count: int
    coinType: SandboxV2CoinType
    value: int
