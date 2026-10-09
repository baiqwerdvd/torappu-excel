from ..common import BaseStruct


class ArkOdcConstData(BaseStruct):
    defaultSceneId: str
    defaultLoadingId: str
    playerSpineName: str
    idleSpecialAnimName: str
    idleSpecialAnimInterval: float
    resetExpIds: list[str]
    npcSelectedFx: str
    interactSelectedFx: str
    sceneValidPositionY: float
