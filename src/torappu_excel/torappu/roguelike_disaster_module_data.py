from ..common import BaseStruct


class RoguelikeDisasterModuleData(BaseStruct):
    disasterData: dict[str, "RoguelikeDisasterModuleData.RoguelikeDisasterData"]

    class RoguelikeDisasterData(BaseStruct):
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
