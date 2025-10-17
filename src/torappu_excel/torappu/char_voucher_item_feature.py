from .voucher_display_type import VoucherDisplayType
from ..common import BaseStruct


class CharVoucherItemFeature(BaseStruct):
    displayType: VoucherDisplayType
    id: str
