from pydantic import BaseModel, ConfigDict

from .act_multi_v3_identity_type import ActMultiV3IdentityType


class ActMultiV3IdentityData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    picId: str
    type: ActMultiV3IdentityType
    maxNum: int
    color: str | None
