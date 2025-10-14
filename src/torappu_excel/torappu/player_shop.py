from pydantic import BaseModel, ConfigDict

from .player_cash_progress_data import PlayerCashProgressData
from .player_classic_qcshop_progress_data import PlayerClassicQCShopProgressData
from .player_common_shop_progress_data import PlayerCommonShopProgressData
from .player_epgsprogress_data import PlayerEPGSProgressData
from .player_furniture_shop_data import PlayerFurnitureShopData
from .player_gift_progress_data import PlayerGiftProgressData
from .player_high_qcshop_progress_data import PlayerHighQCShopProgressData
from .player_lmtgsprogress_data import PlayerLMTGSProgressData
from .player_low_qcshop_progress_data import PlayerLowQCShopProgressData
from .player_skin_shop_data import PlayerSkinShopData
from .player_social_shop_data import PlayerSocialShopData


class PlayerShop(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    LS: PlayerLowQCShopProgressData
    HS: PlayerHighQCShopProgressData
    CLASSIC: PlayerClassicQCShopProgressData
    ES: PlayerCommonShopProgressData
    LMTGS: PlayerLMTGSProgressData
    EPGS: PlayerEPGSProgressData
    REP: PlayerEPGSProgressData
    CASH: PlayerCashProgressData
    GP: PlayerGiftProgressData
    SOCIAL: PlayerSocialShopData
    FURNI: PlayerFurnitureShopData
    SKIN: PlayerSkinShopData
