from pydantic import BaseModel, ConfigDict

from .sandbox_v2_base_update_function_preview_detail_data import SandboxV2BaseUpdateFunctionPreviewDetailData


class SandboxV2BaseFunctionPreviewData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    previewId: str
    previewValue: int
    detailData: SandboxV2BaseUpdateFunctionPreviewDetailData
