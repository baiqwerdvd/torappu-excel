from pydantic import BaseModel, ConfigDict

from .fifth_anniv_explore_value_type import FifthAnnivExploreValueType


class FifthAnnivExploreGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    desc: str
    code: str
    iconId: str
    initialValues: dict[str, int]
    heritageValueType: FifthAnnivExploreValueType
