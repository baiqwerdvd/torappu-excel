from pydantic import BaseModel, ConfigDict


class SpDynIllustInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skinId: str
    spDynIllustId: str
    spDynIllustSkinTag: str
    spIllustId: str
