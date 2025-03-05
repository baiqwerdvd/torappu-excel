from .sandbox_v2_base_update_function_preview_detail_data import SandboxV2BaseUpdateFunctionPreviewDetailData
from ..common import BaseStruct


class SandboxV2BaseFunctionPreviewData(BaseStruct):
    previewId: str
    previewValue: int
    detailData: SandboxV2BaseUpdateFunctionPreviewDetailData
