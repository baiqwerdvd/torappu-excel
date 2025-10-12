from pydantic import BaseModel, ConfigDict

from .sandbox_v2_base_function_preview_data import SandboxV2BaseFunctionPreviewData
from .sandbox_v2_base_update_condition import SandboxV2BaseUpdateCondition


class SandboxV2BaseUpdateData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    baseLevelId: str
    baseLevel: int
    conditions: list[SandboxV2BaseUpdateCondition]
    items: dict[str, int]
    previewDatas: list[SandboxV2BaseFunctionPreviewData]
    scoreFactor: str
    portableRepairCost: int
    entryCount: int
    repairCost: int
