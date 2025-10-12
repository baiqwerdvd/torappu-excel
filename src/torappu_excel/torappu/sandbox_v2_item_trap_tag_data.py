from pydantic import BaseModel, ConfigDict

from .sandbox_v2_item_trap_tag import SandboxV2ItemTrapTag


class SandboxV2ItemTrapTagData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tag: SandboxV2ItemTrapTag
    tagName: str
    tagPic: str
    sortId: int
