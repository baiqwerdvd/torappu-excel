from .ark_odc_basic_data import ArkOdcBasicData
from .arkvent_data import ArkventData
from ..common import BaseStruct


class ArkOdcTable(BaseStruct):
    odcDataMap: dict[str, ArkOdcBasicData]
    arkventDataMap: dict[str, ArkventData]
