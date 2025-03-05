from .item_bundle import ItemBundle
from ..common import BaseStruct


class PotentialMaterialConverterConfig(BaseStruct):
    items: dict[str, ItemBundle]
