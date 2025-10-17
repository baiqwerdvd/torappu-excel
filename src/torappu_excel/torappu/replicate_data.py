from .item_bundle import ItemBundle
from ..common import BaseStruct


class ReplicateData(BaseStruct):
    item: ItemBundle
    replicateTokenItem: ItemBundle
