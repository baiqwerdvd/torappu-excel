from pydantic import BaseModel, ConfigDict


class PlayerCrisisSocialInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    assistCnt: int
    maxPnt: int
    chars: "list[PlayerCrisisSocialInfo.AssistChar]"

    class AssistChar(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        cnt: int
