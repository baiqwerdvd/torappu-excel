from pydantic import BaseModel, ConfigDict


class FifthAnnivExploreBroadcastData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    eventCount: int
    stageId: str
    content: str
