from pydantic import BaseModel, ConfigDict


class CharSkinGroupInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skinGroupId: str
    publishTime: int
