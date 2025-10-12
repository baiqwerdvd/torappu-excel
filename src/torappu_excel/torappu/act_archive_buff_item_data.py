from pydantic import BaseModel, ConfigDict


class ActArchiveBuffItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffId: str
    buffGroupIndex: int
    innerSortId: int
    name: str
    iconId: str
    usage: str
    desc: str
    color: str
