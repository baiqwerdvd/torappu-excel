from .sandbox_v2_data import SandboxV2Data
from ..common import BaseStruct


class SandboxPermDetailData(BaseStruct):
    SANDBOX_V2: dict[str, SandboxV2Data]
