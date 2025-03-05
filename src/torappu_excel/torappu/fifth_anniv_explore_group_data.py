from .fifth_anniv_explore_value_type import FifthAnnivExploreValueType
from ..common import BaseStruct

from msgspec import field


class FifthAnnivExploreGroupData(BaseStruct):
    id_: str = field(name="id")
    name: str
    desc: str
    code: str
    iconId: str
    initialValues: dict[str, int]
    heritageValueType: FifthAnnivExploreValueType
