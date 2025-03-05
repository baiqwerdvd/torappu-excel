from ..common import BaseStruct

from msgspec import field


class RoguelikeDisasterModuleData(BaseStruct):
    class RoguelikeDisasterData(BaseStruct):
        id_: str = field(name="id")
        iconId: str
        toastIconId: str
        level: int
        name: str
        levelName: str
        type_: str = field(name="type")
        functionDesc: str
        desc: str
        sound: str | None

    disasterData: dict[str, "RoguelikeDisasterModuleData.RoguelikeDisasterData"]
