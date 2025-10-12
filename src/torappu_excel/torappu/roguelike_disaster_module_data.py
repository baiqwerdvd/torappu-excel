from pydantic import BaseModel, ConfigDict


class RoguelikeDisasterModuleData(BaseModel):
    class RoguelikeDisasterData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        iconId: str
        toastIconId: str
        level: int
        name: str
        levelName: str
        type: str
        functionDesc: str
        desc: str
        sound: str | None

    disasterData: dict[str, "RoguelikeDisasterModuleData.RoguelikeDisasterData"]
