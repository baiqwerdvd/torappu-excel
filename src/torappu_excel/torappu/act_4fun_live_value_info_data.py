from pydantic import BaseModel, ConfigDict


class Act4funLiveValueInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    liveValueId: str
    name: str
    stageId: str
    iconId: str
    highEndingId: str
    lowEndingId: str
    increaseToastTxt: str
    decreaseToastTxt: str
