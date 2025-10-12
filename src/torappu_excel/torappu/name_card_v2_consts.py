from pydantic import BaseModel, ConfigDict


class NameCardV2Consts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    defaultNameCardSkinId: str
    canUidHide: bool
    removableModuleMaxCount: int
