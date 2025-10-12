from pydantic import BaseModel, ConfigDict

from .sandbox_v2_data import SandboxV2Data


class SandboxPermDetailData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    SANDBOX_V2: dict[str, SandboxV2Data]
