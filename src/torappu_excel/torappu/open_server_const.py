from pydantic import BaseModel, ConfigDict


class OpenServerConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    firstDiamondShardMailCount: int
    initApMailEndTs: int
    resFullOpenUnlockStageId: str
    resFullOpenDuration: int
    resFullOpenTitle: str
    resFullOpenDesc: str
    resFullOpenGuideGroupThreshold: str
    resFullOpenStartTime: int
