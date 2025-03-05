from .replicate_data import ReplicateData
from ..common import BaseStruct


class ReplicateTable(BaseStruct):
    replicateList: list[ReplicateData]
