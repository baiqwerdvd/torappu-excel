from pydantic import BaseModel, ConfigDict

from .act_4fun_cmt_info import Act4funCmtInfo


class Act4funCmtGroupInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    cmtGroupId: str
    cmtList: list[Act4funCmtInfo]
