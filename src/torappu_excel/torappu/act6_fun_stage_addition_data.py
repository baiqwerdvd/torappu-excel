from pydantic import BaseModel, ConfigDict


class Act6FunStageAdditionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    description: str
    npcDialogText: str
    previewCharPicId: str
    feverCoinNum: int
    isHiddenStage: bool
