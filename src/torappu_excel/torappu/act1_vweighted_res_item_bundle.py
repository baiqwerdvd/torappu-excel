from ..common import BaseStruct


class Act1VWeightedResItemBundle(BaseStruct):
    weight: float
    resources: dict[str, int]
