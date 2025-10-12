from pydantic import BaseModel, ConfigDict


class SandboxV2EventSceneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    eventSceneId: str
    title: str
    desc: str
    choiceIds: list[str]
