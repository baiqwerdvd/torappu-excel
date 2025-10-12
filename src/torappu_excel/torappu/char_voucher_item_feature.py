from pydantic import BaseModel, ConfigDict

from .voucher_display_type import VoucherDisplayType


class CharVoucherItemFeature(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    displayType: VoucherDisplayType
    id: str
