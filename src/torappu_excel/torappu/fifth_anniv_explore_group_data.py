from .fifth_anniv_explore_value_type import FifthAnnivExploreValueType
from ..common import BaseStruct


class FifthAnnivExploreGroupData(BaseStruct):
    id: str
    name: str
    desc: str
    code: str
    iconId: str
    initialValues: dict[str, int]
    heritageValueType: FifthAnnivExploreValueType
