from .sandbox_v2_base_unlock_func_display_type import SandboxV2BaseUnlockFuncDisplayType
from .sandbox_v2_base_unlock_func_type import SandboxV2BaseUnlockFuncType
from ..common import BaseStruct


class SandboxV2BaseUpdateFunctionPreviewDetailData(BaseStruct):
    funcId: str
    unlockType: SandboxV2BaseUnlockFuncType
    typeTitle: str
    desc: str
    icon: str
    darkMode: bool
    sortId: int
    displayType: SandboxV2BaseUnlockFuncDisplayType
