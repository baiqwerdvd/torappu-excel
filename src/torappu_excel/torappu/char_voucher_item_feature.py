from .voucher_display_type import VoucherDisplayType
from ..common import BaseStruct

from msgspec import field


class CharVoucherItemFeature(BaseStruct):
    displayType: VoucherDisplayType
    id_: str = field(name="id")
