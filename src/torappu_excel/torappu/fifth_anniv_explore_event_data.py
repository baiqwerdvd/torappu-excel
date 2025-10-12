from pydantic import BaseModel, ConfigDict


class FifthAnnivExploreEventData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    typeName: str
    iconId: str
    desc: str
    choiceIds: list[str]
