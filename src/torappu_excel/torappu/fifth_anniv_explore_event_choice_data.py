from pydantic import BaseModel, ConfigDict


class FifthAnnivExploreEventChoiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    eventId: str
    name: str
    desc: str
    successDesc: str
    failureDesc: str
