from pydantic import BaseModel, ConfigDict

from .sandbox_v2_confirm_icon_type import SandboxV2ConfirmIconType


class SandboxV2ConfirmIconData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    iconType: SandboxV2ConfirmIconType
    iconPicId: str
