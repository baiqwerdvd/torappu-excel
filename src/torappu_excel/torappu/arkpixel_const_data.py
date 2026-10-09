from ..common import BaseStruct


class ArkpixelConstData(BaseStruct):
    arkpixelBagNum: int
    arkpixelOtherPlayerBagNum: int
    maxReleaseTimesPerStage: int
    pixelParamId: str
    hiddenCreatorName: str
    scenePixelDisplayRadius: float
    pixelShowLimitConfigList: list[int]
    showCollectIconCount: int
    maxCollectedCount: int
    maxCollectedDisplayText: str
