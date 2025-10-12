from pydantic import BaseModel, ConfigDict


class Act5FunChoiceRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    choiceId: str
    name: str
    percentage: float | int
    isSpecialStyle: bool
