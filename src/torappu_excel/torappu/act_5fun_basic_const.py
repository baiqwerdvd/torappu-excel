from pydantic import BaseModel, ConfigDict


class Act5funBasicConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storyStageId: str
    betStageId: str
    storyRoundNumber: int
    betRoundNumber: int
    minFundDrop: int
    maxFund: int
