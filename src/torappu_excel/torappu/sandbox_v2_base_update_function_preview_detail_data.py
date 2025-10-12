from pydantic import BaseModel, ConfigDict

from .sandbox_v2_base_unlock_func_display_type import SandboxV2BaseUnlockFuncDisplayType
from .sandbox_v2_base_unlock_func_type import SandboxV2BaseUnlockFuncType


class SandboxV2BaseUpdateFunctionPreviewDetailData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    funcId: str
    unlockType: SandboxV2BaseUnlockFuncType
    typeTitle: str
    desc: str
    icon: str
    darkMode: bool
    sortId: int
    displayType: SandboxV2BaseUnlockFuncDisplayType
