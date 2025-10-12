from pydantic import BaseModel, ConfigDict


class Act6FunConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    defaultStage: str | None
    achievementMaxNumber: int
    specialNumber: int
    characterTipToast: str | None
    functionToastList: list[str] | None
