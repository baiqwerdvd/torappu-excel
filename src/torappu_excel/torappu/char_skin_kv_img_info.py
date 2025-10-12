from pydantic import BaseModel, ConfigDict


class CharSkinKvImgInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    kvImgId: str
    linkedSkinGroupId: str
