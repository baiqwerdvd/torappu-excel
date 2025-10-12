from pydantic import BaseModel, ConfigDict

from .shop_cond_trig_package_type import ShopCondTrigPackageType


class ShopClientGPData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    displayName: str
    condTrigPackageType: ShopCondTrigPackageType
