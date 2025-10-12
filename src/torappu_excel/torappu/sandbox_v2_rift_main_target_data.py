from pydantic import BaseModel, ConfigDict

from .sandbox_v2_rift_main_target_type import SandboxV2RiftMainTargetType


class SandboxV2RiftMainTargetData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    title: str
    desc: str
    storyDesc: str
    targetDayCount: int
    targetType: SandboxV2RiftMainTargetType
    questIconId: str | None
    questIconName: str | None
